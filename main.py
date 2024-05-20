"""Mail parser."""

import os
import traceback

from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI

from open_ai.gpt_openai import analizar_correo
from prompts import PROMPTS
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
        cuerpo = data["cuerpo"]

        try:
            analizar_correo(cuerpo, PROMPTS[remitente])
        except Exception as error:
            print(traceback.format_exc())
            print(f"No se pudo extraer informacion del correo: {error}")

    except Exception as error:
        print(f"error: {error}")
        raise


@app.post("/")
async def notificaciones(background_tasks: BackgroundTasks) -> str:
    """Función que escucha al correo de gmail cada vez que llega un correo."""
    background_tasks.add_task(main)
    return ""
