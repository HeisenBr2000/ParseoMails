"""Mail parser."""

from fastapi import FastAPI, Request

from utils import obtener_ultimo_correo


app = FastAPI()


@app.post("/")
async def notificacionesUser(request: Request):
    """Recibir notificaciones de pub/sub de un nuevo correo en la bandeja."""
    print(await request.json())
    obtener_ultimo_correo()
    return {}
