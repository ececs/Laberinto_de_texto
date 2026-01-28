
"""
acciones.py
===========
Este módulo se encarga de las acciones que puede realizar el jugador
sobre el mundo del juego.

Permite:
- Coger y soltar objetos.
- Consultar el inventario.
- Inspeccionar objetos para obtener información.

Usa:
- estado.py para acceder y modificar el inventario y la ubicación.
- mundo.py para comprobar qué objetos hay en cada sala.
"""

import estado
import mundo
# Diccionario que guarda descripción corta de cada objeto. 
# Cuando el jugador escribe inspeccionar llave, devuelve un texto.
OBJ_DESCS = {
    "llave": "Una llave pequeña y vieja, parece estar muy oxidada.",
    "pergamino": "Un pergamino con símbolos borrosos, puede que sirva de algo.",
    "medallon": "Un medallón frío al tacto, si fuera de oro no estaría rallado.",
    "antorcha": "Podría encenderse, pero hace falta fuego.",
}
# Función coger. Mira en que sala estas, pide a mundo.py la lista de objetos visibles de la sala. 
# Si no está, devuelve mensaje.
def coger(obj: str) -> str:
    objs = mundo.objetos_visibles(estado.ubicacion)
    if obj not in objs:
        return f"No hay '{obj}' aquí."
# Si está, lo quita de la sala(remove) y lo mete en inventario(append).
    mundo.OBJETOS_EN_SALA[estado.ubicacion].remove(obj)
    estado.inventario.append(obj)
# Finalmente devuelve texto de confirmación.
    return f"Has cogido '{obj}'."

# Función soltar.Comprueba si el objeto está en inventario.
# Si no lo tienes, devuelve un mensaje.
def soltar(obj: str) -> str:
    if obj not in estado.inventario:
        return f"No tienes '{obj}'."
# Si lo tienes lo quita del inventario(remove).
# Lo añade en la sala actual(append).
# Devuelve confirmación.
    estado.inventario.remove(obj)
    mundo.OBJETOS_EN_SALA[estado.ubicacion].append(obj)
    return f"Has soltado '{obj}'."

# Función inventario. Si tiene cosas, las une con comas, si está vacio, lo muestra.
def inventario() -> str:
    return "Inventario: " + (", ".join(estado.inventario) if estado.inventario else "(vacío)")

# Función inspeccionar objetos.
def inspeccionar(obj: str) -> str:
    # Comprueba si el objeto es el pergamino.
    # El pergamino solo se puede leer si está en el inventario.
    if obj == "pergamino":
        if obj not in estado.inventario:
            return "El pergamino está ahí, pero necesitas cogerlo para poder leerlo."
        return (
            "Desenrollas el pergamino y lees:\n"
            "\"Allí donde el agua cae en la oscuridad,\n"
            "el camino hacia la libertad apunta al norte.\n"
            "Pero ninguna puerta cede ante manos vacías.\""
        )
    # Comprueba si el objeto está en tu inventario o visible en la sala actual.
    # Si está devuelve descripción, si no frase genérica.
    # Si el objeto no está ni en inventario ni en sala, devuelve "No ves"
    if obj in estado.inventario or obj in mundo.objetos_visibles(estado.ubicacion):
        return OBJ_DESCS.get(obj, f"No ves nada especial en '{obj}'.")
    return f"No ves '{obj}'."

