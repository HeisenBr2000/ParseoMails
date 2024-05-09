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

async def servicio_gmail(credencial):
    service = build('gmail', 'v1', credentials=credencial)
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=1).execute()
    messages = results.get('messages', [])
    return messages

@api.post("/")
async def notificacionesUser(request : Request):
    data = await request.json()
    print("Tienes un correo entrante...\n", data)
    return {}

