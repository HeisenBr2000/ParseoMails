"""Funciones de utilidad."""

import base64
import re

from gmail.gmail import obtener_servicio_gmail


def obtener_asunto(headers: dict) -> str:
    """Función que obtiene el asunto del correo."""
    return next((header["value"] for header in headers if header["name"] == "Subject"), "")


def obtener_remitente(headers: dict) -> str:
    """Obtener el email del remitente."""
    remitente = next(header["value"] for header in headers if header["name"] == "From")
    if match := re.search(r"<(.+?)>", remitente):
        return match[1]
    raise ValueError("No se pudo detectar el remitente")


def obtener_cuerpo(message: dict) -> str:
    """Función que obtiene el cuerpo del correo."""
    if "parts" in message["payload"]:
        for part in message["payload"]["parts"]:
            if part["mimeType"] == "text/plain":
                data = part["body"]["data"]
                return base64.urlsafe_b64decode(data).decode("utf-8")
    return ""


def extraer_info_correo(email: str) -> dict[str, str]:
    """Función que extrae el remitente, asunto y cuerpo del correo."""
    gmail = obtener_servicio_gmail(email)
    results = gmail.users().messages().list(userId=email, maxResults=1).execute()
    messages = results.get("messages", [])

    message = messages[0]
    email_data = gmail.users().messages().get(userId=email, id=message["id"]).execute()
    headers = email_data["payload"]["headers"]
    sender = obtener_remitente(headers)
    subject = obtener_asunto(headers)
    body = obtener_cuerpo(email_data)

    return {"remitente": sender, "asunto": subject, "cuerpo": body}
