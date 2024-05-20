"""Módulo para interactuar con la api de gmail."""

from typing import Any

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def obtener_servicio_gmail(email: str) -> Any:
    """Obtiene servicio de gmail."""
    service_account_file = "boost-1minaldia-c63063e85064.json"
    scopes = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/pubsub"]
    credentials: Credentials = Credentials.from_service_account_file(service_account_file, scopes=scopes)
    delegated_credentials: Credentials = credentials.with_subject(email)
    return build("gmail", "v1", credentials=delegated_credentials)
