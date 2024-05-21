"""Template básico para construir prompts."""

from string import Template

template = Template(
    """
Eres un asistente encargado de extraer información de correos electrónicos.

Te pasaré el asunto y el cuerpo de un email como string. El email puede contener tanto texto plano como HTML.

$contexto

El objetivo es extraer o inferir desde el asunto y cuerpo del email los siguientes datos:
$datos

Quiero que extraigas los datos y me entregues el resultado en formato JSON.
La estructura del resultado y los nombres de las llaves DEBEN ser así:
$output

Reglas para el formato JSON:
- La respuesta DEBE ser un JSON válido, sin saltos de línea entre las llaves del objeto JSON.
- Si un dato no es posible obtenerlo ni inferirlo, se le debe asignar el valor 'null'.
- Si te pido un RUT siempre debe estar en formato con guión y dígito verificador, por ejemplo, '19278540-5'.
- Si te pido un email siempre debe estar en minúsculas, por ejemplo: 'jhon@mail.com'.
- Si te pido un teléfono siempre de estar en el formato de 11 dígitos solo con caractéres numéricos, por ejemplo: '56973695471'

Ayuda para identificar patrones:
$hints

A continuación de dejo unos ejemplos del formato de salida válido:
$ejemplos

El asunto del correo es el siguiente:
$asunto

El cuerpo del correo es el siguiente:
$cuerpo
"""
)


def prompt_constructor(datos: dict, asunto: str, cuerpo: str) -> str:
    """Constructor del prompt a partir de los datos."""
    required_keys = ["contexto", "datos", "output", "hints", "ejemplos"]

    for key in required_keys:
        if key not in datos:
            raise ValueError(f"Falta el dato requerido: {key}")

    contexto = datos["contexto"]
    datos_a_extraer = list_to_bullet_string(datos["datos"])
    output = datos["output"]
    hints = list_to_bullet_string(datos["hints"])
    ejemplos = datos["ejemplos"]

    return template.substitute(
        contexto=contexto,
        datos=datos_a_extraer,
        output=output,
        hints=hints,
        ejemplos=ejemplos,
        asunto=asunto,
        cuerpo=cuerpo,
    )


def list_to_bullet_string(items: list[str]) -> str:
    """Convierte una lista de elementos en un string con formato de lista con viñetas."""
    return "\n".join(f"- {item}" for item in items)
