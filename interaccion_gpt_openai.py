import os

import openai
from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()
client = OpenAI()


# Función de prueba interacción OpenAI
def test_openai():
    """Función de prueba OpenAI."""
    client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Eres un profesor que da clases en ingles",
            },
            {"role": "user", "content": "Realiza algunos ejercicios para entender ingles"},
        ],
    )
    print(completion.choices[0].message)


test_openai()

def analisis_correo(email_body, prompt, output):

