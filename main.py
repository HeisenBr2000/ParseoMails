"""Mail parser."""

from fastapi import FastAPI, Request
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
# from utils import obtener_ultimo_correo


app = FastAPI()


def obtener_servicio_gmail(email: str):
    SERVICE_ACCOUNT_FILE = "boost-1minaldia-c63063e85064.json"
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    credentials: Credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    delegated_credentials: Credentials = credentials.with_subject(email)
    return build("gmail", "v1", credentials=delegated_credentials)


@app.post("/")
async def notificacionesUser(request: Request):
    """Recibir notificaciones de pub/sub de un nuevo correo en la bandeja."""
    print(await request.json())
    gmail = obtener_servicio_gmail("matias@boostapp.cl")
    results = gmail.users().messages().list(userId="me").execute()
    messages = results.get("messages", [])
    for message in messages[:3]:
        msg_id = message["id"]
        msg = (
            gmail.users()
            .messages()
            .get(userId="me", id=msg_id, format="full")
            .execute()
        )

        headers = msg["payload"]["headers"]
        subject = next(
            (header["value"] for header in headers if header["name"] == "Subject"),
            None,
        )
        print(f"Message ID: {msg_id}, Subject: {subject}")

    return {"chao": "holaaaaaa"}
