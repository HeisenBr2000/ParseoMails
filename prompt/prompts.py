"""Datos para armar el prompt de cada remitente."""

clientes = {
    "mglasner10@gmail.com": {
        "contexto": "El email consiste en una notificación de un portal inmobiliario, sobre un cliente potencial interesado en uno de nuestros departamentos en venta o arriendo.",
        "datos": [
            "nombre del cliente",
            "email del cliente",
            "teléfono del cliente",
            "nombre del proyecto o edificio",
            "identificador del departamento",
        ],
        "output": "{'cliente':{'nombre':'nombre del cliente','email':'email del cliente','telefono':'teléfono del cliente'},'proyecto':{'nombre':'nombre del proyecto o edificio','departamento':'identificador del departamento'}}",
        "hints": [
            "Los proyectos se llaman: 'Seminario A', 'Seminario B', 'Hernán Cortés' o 'Campoamor', debes asignar uno de esos nombres al proyecto, si no es posible determinarlo asignar 'null'",
            "Los departamentos normalmente se identifican por un número o una letra.",
            "Es común que el identificador del departamento venga a continuación del nombre del proyecto.",
        ],
        "ejemplos": "{'cliente':{'nombre':'jhon doe','email':'jhon@mail.com','telefono':'56932548716'},'proyecto':{'nombre':'edificio seminario','departamento':'C'}}",
    },
    "matias@boostapp.cl": {
        "contexto": "El email consiste en una notificación de un portal inmobiliario, sobre un cliente potencial interesado en uno de nuestros departamentos en venta o arriendo.",
        "datos": [
            "nombre del cliente",
            "email del cliente",
            "teléfono del cliente",
            "nombre del proyecto o edificio",
            "identificador del departamento",
        ],
        "output": "{'cliente':{'nombre':'nombre del cliente','email':'email del cliente','telefono':'teléfono del cliente'},'proyecto':{'nombre':'nombre del proyecto o edificio','departamento':'identificador del departamento'}}",
        "hints": [
            "Los proyectos se llaman: 'Seminario A', 'Seminario B', 'Hernán Cortés' o 'Campoamor', debes asignar uno de esos nombres al proyecto, si no es posible determinarlo asignar 'null'",
            "Los departamentos normalmente se identifican por un número o una letra.",
            "Es común que el identificador del departamento venga a continuación del nombre del proyecto.",
        ],
        "ejemplos": "{'cliente':{'nombre':'jhon doe','email':'jhon@mail.com','telefono':'56932548716'},'proyecto':{'nombre':'edificio seminario','departamento':'C'}}",
    },
}
