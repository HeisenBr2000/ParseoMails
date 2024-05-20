import os

import openai
from fastapi import FastAPI

app = FastAPI()


# Función de prueba interacción OpenAI
def analizar_correo(email_body: str, subject_email: str, prompt: str, output: dict):
    """Función de prueba OpenAI."""
    client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))
    messages = [
        {"role": "system", "content": "Eres un asistente que ayuda a extraer informacion de correos electronicos"},
        {"role": "user", "content": f"{prompt}Asunto:{subject_email}Cuerpo del correo:{email_body}"},
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    output_text = response.choices[0].message.content
    output_lines = output_text.split("\n")

    for idx, line in enumerate(output_lines):
        line = line.strip()
        if line:
            output[f"{idx+1}"] = line
    return output
