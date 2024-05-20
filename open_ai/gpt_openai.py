"""Módulo para interactuar con la api de openai."""

import json
import os
from json.decoder import JSONDecodeError

import openai


def analizar_correo(body: str, prompt: str) -> None:
    """Función de prueba OpenAI."""
    client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente que ayuda a extraer informacion de correos electrónicos"},
            {"role": "user", "content": prompt},
            {"role": "user", "content": body},
        ],
    )

    try:
        print(json.loads(completion.choices[0].message.content))
    except JSONDecodeError:
        print("fallo la conversion a json")
