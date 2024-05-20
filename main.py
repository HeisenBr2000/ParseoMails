"""Mail parser."""

from fastapi import FastAPI, Request

from interaccion_gpt_openai import analizar_correo
from utils import extraer_info_correo, leer_prompt

app = FastAPI()


@app.post("/")
async def notificaciones_user(request: Request) -> str:
    """Función que escucha al correo de gmail cada vez que llega un correo."""
    email = "matias@boostapp.cl"
    if correo_info := extraer_info_correo(email):
        email_body = correo_info[0]["cuerpo"]
        subject_email = correo_info[0]["asunto"]
        prompt = leer_prompt("prompt.json")

        try:
            analizar_correo(email_body, subject_email, prompt)
        except Exception:
            print("No se pudo extraer informacion del correo")

    return ""
