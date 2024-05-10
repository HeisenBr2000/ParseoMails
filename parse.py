from fastapi import FastAPI, Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import base64

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

credencial = credenciales()

def obtener_ultimo_correo():
    service = build('gmail', 'v1', credentials=credencial)
    # Muestra la lista de mensajes/correos que han llegado
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    if messages:
        message_id = messages[0]['id']
        # Recupera el ultimo mensaje/correo que ha llegado
        message = service.users().messages().get(userId='me', id=message_id).execute()
        headers = message['payload']['headers']
        subject = next((header['value'] for header in headers if header['name'] == 'Subject'), None)
        sender = next((header['value'] for header in headers if header['name'] == 'From'), None)
        body = message['snippet']
        return {"Asunto": subject, "Remitente": sender, "Cuerpo": body}
    else:
        return {"message": "No se encontraron correos en la bandeja de entrada"}


@api.post("/")
async def notificacionesUser(request: Request):
    print (request)
    detalles_correo = obtener_ultimo_correo()
    print("Tienes un correo entrante...", detalles_correo)
    return {}



