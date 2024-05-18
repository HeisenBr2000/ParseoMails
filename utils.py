"""Funciones de utilidad."""

import base64

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def obtener_servicio_gmail(email: str):
    """Obtiene servicio de gmail."""
    service_account_file = "boost-1minaldia-c63063e85064.json"
    scopes = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/pubsub"]
    credentials: Credentials = Credentials.from_service_account_file(service_account_file, scopes=scopes)
    delegated_credentials: Credentials = credentials.with_subject(email)
    return build("gmail", "v1", credentials=delegated_credentials)


def obtener_asunto(headers):
    """Función que obtiene el asunto del correo."""
    sender = next(header["value"] for header in headers if header["name"] == "Subject")
    return sender


def obtener_remitente(headers):
    """Función que obtiene el encabezado del correo."""
    subject = next(header["value"] for header in headers if header["name"] == "From")
    return subject


def obtener_cuerpo(message):
    """Función que obtiene el cuerpo del correo."""
    if "parts" in message["payload"]:
        parts = message["payload"]["parts"]
        for part in parts:
            if part["mimeType"] == "text/plain":
                data = part["body"]["data"]
                body = base64.urlsafe_b64decode(data).decode("utf-8")
                return body


# Guardar funcion que extrae remitente, asunto y cuerpo del correo #
def extraer_info_correo(email: str):
    """Función que extrae el remitente, asunto y cuerpo del correo."""
    gmail = obtener_servicio_gmail(email)
    results = gmail.users().messages().list(userId=email).execute()
    messages = results.get("messages", [])

    correos_info = []
    for message in messages:
        message_id = message["id"]
        message = gmail.users().messages().get(userId=email, id=message_id).execute()
        headers = message["payload"]["headers"]
        sender = obtener_remitente(headers)
        subject = obtener_asunto(headers)
        body = obtener_cuerpo(message)

        correo_info = {"Remitente": sender, "Asunto": subject, "Cuerpo": body}

        correos_info.append(correo_info)
        return correos_info
