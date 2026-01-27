"""
estado.py
=========
Este archivo guarda el estado del juego.

Aquí se almacenan los datos que cambian mientras el jugador juega,
como:
- La sala en la que se encuentra.
- Los objetos del inventario.
- Las salas ya visitadas.
- Si el jugador ha ganado la partida.

Otros módulos consultan y modifican este estado durante el juego.
"""

# Sala en la que empieza el jugador
ubicacion = "entrada"

# Lista con los objetos que lleva el jugador
inventario = []

# Conjunto de salas que el jugador ya ha visitado
visitadas = set()

# Indica si el jugador ha ganado el juego
victoria = False


def resetear():
# Función para volver el juego a su estado inicial.
    """
    Reinicia el estado del juego a los valores iniciales.
    Se usaría si empezamos una nueva partida.
    """
# Modificamos varibles globales, estan arriba, fuera de la función.
    global ubicacion, inventario, visitadas, victoria

    ubicacion = "entrada"
    inventario = []
    visitadas = set()
    victoria = False
