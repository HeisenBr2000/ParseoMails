"""Funciones de utilidad."""

import base64
import re
from googleapiclient.discovery import build
from google.oauth2 import service_account


def obtener_credenciales():
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    SERVICE_ACCOUNT_FILE = (
        "credentials.json"  # Ruta al archivo JSON de la cuenta de servicio
    )

    return service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )


def obtener_ultimo_correo():
    service = build("gmail", "v1", credentials=obtener_credenciales())

    # Muestra la lista de mensajes/correos que han llegado
    results = service.users().messages().list(userId="me", labelIds=["INBOX"]).execute()
    if messages := results.get("messages", []):
        message_id = messages[0]["id"]
        # Recupera el ultimo mensaje/correo que ha llegado
        message = service.users().messages().get(userId="me", id=message_id).execute()
        headers = message["payload"]["headers"]

        subject = next(
            header["value"] for header in headers if header["name"] == "Subject"
        )
        sender = next(header["value"] for header in headers if header["name"] == "From")
        body = obtener_cuerpo(
            message
        )  # Asumiendo que tienes una función para extraer el cuerpo del correo

        print({"Asunto": subject, "Remitente": sender, "Cuerpo": body})
        return {"Asunto": subject, "Remitente": sender, "Cuerpo": body}


def obtener_encabezado(headers, name):
    return next((header["value"] for header in headers if header["name"] == name), None)


# Quitar caracteres de escape con regex
def obtener_cuerpo(message):
    if "parts" in message["payload"]:
        parts = message["payload"]["parts"]
        for part in parts:
            if part["mimeType"] == "text/plain":
                data = part["body"]["data"]
                body = base64.urlsafe_b64decode(data).decode("utf-8")
                body = re.sub(r"[\r\n]", "", body)
                return body
