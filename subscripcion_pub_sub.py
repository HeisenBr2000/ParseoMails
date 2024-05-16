import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Rutas y configuración
SERVICE_ACCOUNT_FILE = "boost-1minaldia-c63063e85064.json"
TOPIC_NAME = "projects/boost-1minaldia/topics/mailParser"

# Alcances necesarios
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/pubsub",
]

# Cargar las credenciales de la cuenta de servicio
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

delegated_credentials = credentials.with_subject("matias@boostapp.cl")

# Construir el cliente de la API de Gmail
service = build("gmail", "v1", credentials=delegated_credentials)


# Configurar las notificaciones de Pub/Sub
def configure_gmail_watch():
    request_body = {"labelIds": ["INBOX"], "topicName": TOPIC_NAME}
    response = service.users().watch(userId="me", body=request_body).execute()
    print("Watch response: ", response)


if __name__ == "__main__":
    configure_gmail_watch()
