"""
Módulo estado.py

Este módulo centraliza el estado de la sesión de juego mediante variables globales.

Gestiona la persistencia de datos dinámicos como la posición del usuario, 
el contenido del inventario y el progreso de la partida (salas visitadas y 
condición de victoria).

Responsabilidades:
- Mantener variables globales que representan el estado actual del juego.
- Proveer una función para reiniciar el estado a los valores iniciales.

Variables principales:
- ubicacion (str): Identificador de la sala actual del jugador.
- inventario (list): Lista de objetos que el jugador ha recogido.
- visitadas (set): Conjunto de salas que el jugador ha visitado.
- victoria (bool): Indica si el jugador ha ganado la partida.

Funciones principales:
- resetear(): Reinicia el estado del juego a los valores iniciales.
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
    """
    Reinicia todas las variables de estado a sus valores por defecto.

    Esta función utiliza la palabra clave 'global' para modificar las variables 
    definidas en el nivel superior del script, asegurando que los cambios 
    persistan en todo el programa.

    :return: No devuelve ningún valor.

    .. note::
       Es fundamental para implementar la funcionalidad de 'reiniciar partida' 
       sin necesidad de cerrar el intérprete de Python.
    """

# Modificamos varibles globales, estan arriba, fuera de la función.
    global ubicacion, inventario, visitadas, victoria

    ubicacion = "entrada"
    inventario = []
    visitadas = set()
    victoria = False
