"""Módulo para interactuar con la api de openai."""

import json
import os
from json.decoder import JSONDecodeError

import openai


def analizar_correo(prompt: str) -> None:
    """Función de prueba OpenAI."""
    client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    try:
        response_content = completion.choices[0].message.content
        if response_content is None:
            raise ValueError(f"No hubo respuesta de gpt {completion.choices}")

        response_content = response_content.replace("'", '"')

        response_json = json.loads(response_content)
        print(response_json)

    except JSONDecodeError:
        print(f"falló la conversion a json. {response_content}")
