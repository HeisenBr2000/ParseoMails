"""Mail parser."""

from fastapi import FastAPI, Request

from interaccion_gpt_openai import analizar_correo
from utils import extraer_info_correo, leer_prompt

app = FastAPI()


@app.post("/")
async def notificaciones_user(request: Request):
    """Función que escucha al correo de gmail cada vez que llega un correo."""
    print(await request.json())
    email = "matias@boostapp.cl"
    correo_info = extraer_info_correo(email)
    print(correo_info)

    if correo_info:
        email_body = correo_info[0]["cuerpo"]
        subject_email = correo_info[0]["asunto"]
        prompt = leer_prompt("prompt.json")
        output = {}

        resultado = analizar_correo(email_body, subject_email, prompt, output)
        print(resultado)
        return resultado
    else:
        return {"error": "No se pudo extraer informacion del correo"}
