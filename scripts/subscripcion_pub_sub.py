"""Script para renovar la subscripción de pub sub."""

import os

from dotenv import load_dotenv

from gmail.gmail import obtener_servicio_gmail

load_dotenv()

SERVICE_ACCOUNT_FILE = "boost-1minaldia-c63063e85064.json"
TOPIC_NAME = "projects/boost-1minaldia/topics/mailParser"


def llamada_correos() -> None:
    """Función que llama al tema pub/sub para publicar notificaciones."""
    email = os.getenv("EMAIL")
    if email is None:
        raise ValueError("Email no detectado")

    service = obtener_servicio_gmail(email)
    request_body = {"labelIds": ["INBOX"], "topicName": TOPIC_NAME}
    response = service.users().watch(userId=email, max_results=1, body=request_body).execute()
    print("Watch response: ", response)


llamada_correos()
