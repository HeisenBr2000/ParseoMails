from utils import obtener_servicio_gmail

# Rutas y configuración
SERVICE_ACCOUNT_FILE = "boost-1minaldia-c63063e85064.json"
TOPIC_NAME = "projects/boost-1minaldia/topics/mailParser"


# Alcances necesarios
def llamada_correos():
    """Función que llama al tema pub/sub para publicar notificaciones."""
    service = obtener_servicio_gmail("matias@boostapp.cl")
    request_body = {"labelIds": ["INBOX"], "topicName": TOPIC_NAME}
    response = service.users().watch(userId="matias@boostapp.cl", body=request_body).execute()
    print("Watch response: ", response)


llamada_correos()
