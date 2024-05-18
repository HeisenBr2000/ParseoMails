"""Mail parser."""

from fastapi import FastAPI, Request

from utils import extraer_info_correo

app = FastAPI()


@app.post("/")
async def notificaciones_user(request: Request):
    """Función que escucha al correo de gmail cada vez que llega un correo."""
    print(await request.json())
    email = "matias@boostapp.cl"
    correo_info = extraer_info_correo(email)
    print(correo_info)
