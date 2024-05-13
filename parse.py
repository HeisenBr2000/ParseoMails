from fastapi import FastAPI, Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import base64
import re

api = FastAPI()

# Paso a paso
# Acceder a las credenciales de gmail 

SCOPES = ['https://www.googleapis.com/auth/gmail.addons.current.message.readonly','https://www.googleapis.com/auth/gmail.modify']

def credenciales():
    flow = InstalledAppFlow.from_client_secrets_file(
        os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), SCOPES)
    flow.redirect_uri = 'http://localhost:8080/'
    credencial = flow.run_local_server()
    flow.authorization_url(
        access_type='offline'
    )
    return credencial



def obtener_encabezado(headers, name):
    for header in headers:
        if header['name'] == name:
            return header['value']
    return None

# Quitar caracteres de escape con regex 
def obtener_cuerpo(message):
    if 'parts' in message['payload']:
        parts = message['payload']['parts']
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                body = base64.urlsafe_b64decode(data).decode('utf-8')
                body = re.sub(r'[\r\n]', '', body)
                return body
            
def obtener_ultimo_correo():
    credencial = credenciales()
    service = build('gmail', 'v1', credentials=credencial)
    # Muestra la lista de mensajes/correos que han llegado
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    if messages:
        message_id = messages[0]['id']
        # Recupera el ultimo mensaje/correo que ha llegado
        message = service.users().messages().get(userId='me', id=message_id).execute()
        headers = message['payload']['headers']
        subject = obtener_encabezado(headers, 'Subject')
        sender = obtener_encabezado(headers, 'From')
        body = obtener_cuerpo(message)

        return {"Asunto": subject, "Remitente": sender, "Cuerpo": body}

@api.post("/")
async def notificacionesUser(request: Request):
    print (request)
    detalles_correo = obtener_ultimo_correo()
    print("Tienes un correo entrante...", detalles_correo)
    return {}

# Interfaz de usuario en la cual el usuario ingrese sus credenciales de correo electronico y contraseña, luego la app utilizara
# esas credenciales para conectarse al servidor del correo y recibir notificaciones sobre nuevos correos electronicos




