"""Mail parser."""

import os
import traceback

from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, Request

from open_ai.gpt_openai import analizar_correo
from prompt.prompts import clientes
from prompt.template import prompt_constructor
from utils import extraer_info_correo

load_dotenv()

app = FastAPI()


def main() -> None:
    """Función principal."""
    try:
        email = os.getenv("EMAIL")
        if email is None:
            raise ValueError("Email no detectado")

        data = extraer_info_correo(email)
        remitente = data["remitente"]
        asunto = data["asunto"]
        cuerpo = data["cuerpo"]

        try:
            analizar_correo(prompt_constructor(clientes[remitente], asunto, cuerpo))
        except Exception as error:
            print(traceback.format_exc())
            print(f"No se pudo extraer informacion del correo: {error}")

    except Exception as error:
        print(f"error: {error}")
        raise


@app.post("/")
async def notificaciones(request: Request, background_tasks: BackgroundTasks) -> str:
    """Función que escucha al correo de gmail cada vez que llega un correo."""
    print(await request.json())
    background_tasks.add_task(main)
    return ""
