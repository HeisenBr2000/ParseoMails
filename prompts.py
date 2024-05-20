"""Prompts por remitente."""

PROMPTS = {
    "mglasner10@gmail.com": """
        Te voy a enviar el cuerpo de un email como string, el email puede contener tanto texto plano como html.
        El email trata sobre una notificación de un cliente interesado en obtener información sobre una propiedad en arriendo.
        El objetivo es extraer desde el cuerpo del email los datos del cliente y de la propiedad.
        Los datos de interés son los siguientes:
          - nombre del cliente
          - email del cliente
          - rut del cliente
          - nombre del proyecto
          - número del departamento

        Quiero que encuentros los datos y me entregues el resultado en formato json.

        Se deben seguir las siguientes reglas para el output en formato json:
        1. Si un dato no está dispobible en el cuerpo del correo devuelve un valor nulo..
        2. El rut siempre entregalo en formato con guión y dígito verificador, por ejemplo '19278540-5'.
        3. El email siempre etrégalo en minúsculas.
        4. Si el email trata de otra cosa, retornar el valor None.
        5. Jamás retornes Markdown, siempre el equivalente como string de un JSON válido.
        6. Tu respuesta debe poder ser pasada directamente al la librería json y al método json.loads de python.
        7. Evita poner saltos de línea '\n' entre las llaves del objeto json.

        A continuación te muestro algunos ejemplos del formato de salida:
        ejemplo 1 (caso en que se encuentran todos los datos):
            '{"cliente": {"nombre": "Jhon Doe","email": "jhon@mail.com","rut": "16020266-1"},"proyecto": {"nombre": "Edificio San Cristobal","departamento": "105"}}'

        ejemplo 2 (caso en que se encuentran datos parciales o incompletos):
            '{"cliente": {"nombre": "Karen Doe","email": "karen@mail.com","rut": null},"proyecto": {"nombre": "Edificio Seminario","departamento": null}}'

        ejemplo 3 (caso en que el email trata de otra cosa):
            '{"cliente": None,"proyecto": None}'

        ejemplo 4 (caso de respuesta no aceptable por contener saltos de línea entre llaves):
            '{\n"cliente": {\n"nombre": "Jhon Doe",\n"email": "jhon@mail.com",\n"rut": "16020266-1"},"proyecto": {"nombre": "Edificio San Cristobal","departamento": "105"}}'
    """,
    "seb.larag@duocuc.cl": "",
}
