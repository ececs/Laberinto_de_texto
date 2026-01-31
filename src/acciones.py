
"""
Módulo acciones.py

Gestiona la lógica de interacción entre el jugador y los objetos 
del mundo. Implementa las funciones necesarias para la manipulación del 
inventario y la inspección detallada de elementos del entorno.

Responsabilidad:
- Proporcionar funciones para coger y soltar objetos.
- Permitir al jugador inspeccionar objetos para obtener descripciones.
- Gestionar el inventario del jugador.

Relaciones:
- Importa: `estado` para acceder al inventario y ubicación del jugador.
- Importa: `mundo` para interactuar con los objetos presentes en las salas.

Funciones principales:
- coger(obj): permite al jugador recoger un objeto de la sala actual.
- soltar(obj): permite al jugador soltar un objeto en la sala actual.
- inventario(): muestra los objetos actualmente en el inventario del jugador.
- inspeccionar(obj): proporciona una descripción detallada de un objeto.
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

def coger(obj: str) -> str:
    """
    Transfiere un objeto desde la habitación actual al inventario del jugador.

    Verifica la existencia del objeto en la sala y, en caso positivo, realiza 
    la mutación de las listas correspondientes en el estado global y el mundo.

    :param obj: Nombre del objeto que se desea recoger.
    :type obj: str
    :return: Mensaje informativo sobre el éxito o fracaso de la acción.
    :rtype: str
    
    .. note::
       Esta función modifica directamente la colección de objetos de la sala 
       en el módulo `mundo`.
    """
    objs = mundo.objetos_visibles(estado.ubicacion)
    if obj not in objs:
        return f"No hay '{obj}' aquí."
# Si está, lo quita de la sala(remove) y lo mete en inventario(append).
    mundo.OBJETOS_EN_SALA[estado.ubicacion].remove(obj)
    estado.inventario.append(obj)
# Finalmente devuelve texto de confirmación.
    return f"Has cogido '{obj}'."

def soltar(obj: str) -> str:
    """
    Deposita un objeto del inventario en la habitación actual.

    Realiza la operación inversa a `coger`, validando primero que el usuario 
    posea el ítem antes de actualizar las estructuras de datos.

    :param obj: Nombre del objeto a descartar.
    :type obj: str
    :return: Confirmación de la acción realizada.
    :rtype: str
    """
    # Comprueba si el objeto está en el inventario.
    if obj not in estado.inventario:
        return f"No tienes '{obj}'."
    # Si lo tienes lo quita del inventario(remove).
    # Lo añade en la sala actual(append).
    # Devuelve confirmación.
    estado.inventario.remove(obj)
    mundo.OBJETOS_EN_SALA[estado.ubicacion].append(obj)
    return f"Has soltado '{obj}'."

def inventario() -> str:
    """
    Genera una representación textual de los objetos que tiene el jugador.

    Aplica lógica condicional para manejar el caso de inventario vacío o 
    formatear la lista de ítems mediante concatenación de cadenas.

    :return: Cadena con la lista de objetos o aviso de inventario vacío.
    :rtype: str
    """

    if estado.inventario:
        return "Inventario: " + ", ".join(estado.inventario)
    else:
        return "Inventario: (vacío)"

def inspeccionar(obj: str) -> str:
    """
    Devuelve la descripción detallada de un objeto si es accesible.

    Comprueba si el objeto está en el inventario o en la sala actual. Incluye 
    lógica especial para el objeto 'pergamino', que requiere estar en posesión 
    del jugador para ser leído.

    :param obj: El nombre del objeto a examinar.
    :type obj: str
    :return: La descripción del objeto o un mensaje de error si no es visible.
    :rtype: str
    
    .. note::
       Si el objeto es 'pergamino', se requiere una validación de seguridad 
       adicional sobre el inventario.
    """
    # Comprueba si el objeto es el pergamino.
    # El pergamino solo se puede leer si está en el inventario.
    if obj == "pergamino":
        if obj not in estado.inventario:
            return "El pergamino está ahí, pero necesitas cogerlo para poder leerlo."
        return (
            "Desenrollas el pergamino y lees:\n\n"
            "\"Allí donde el agua cae en la oscuridad,\n"
            "el camino hacia la libertad apunta al norte.\n"
            "Pero ninguna puerta cede ante manos vacías.\""
        )
    # Comprueba si el objeto está en tu inventario o visible en la sala actual.
    # Si está devuelve descripción, si no frase genérica.
    # Si el objeto no está ni en inventario ni en sala, devuelve "No ves"
    if obj in estado.inventario:
        return OBJ_DESCS.get(obj, f"No ves nada especial en '{obj}'.")

    if obj in mundo.objetos_visibles(estado.ubicacion):
        return OBJ_DESCS.get(obj, f"No ves nada especial en '{obj}'.")

    return f"No ves '{obj}'."