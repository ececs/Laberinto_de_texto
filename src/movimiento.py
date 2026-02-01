"""
Módulo movimiento.py

Implementa la lógica de navegación y exploración del mundo.

Se encarga de gestionar el desplazamiento del usuario entre nodos (habitaciones) 
y de la generación de la interfaz textual descriptiva de cada ubicación, 
interactuando con los estados globales y la base de datos del mundo.
"""

import estado
import mundo


def mirar() -> str:
    """
    Construye la representación textual de la ubicación actual del jugador.

    Consulta el módulo `mundo` para obtener los metadatos de la sala, 
    los objetos presentes y las conexiones disponibles, formateando la 
    información para su visualización en consola.

    :return: Un string detallado con la descripción, objetos y salidas.
    :rtype: str
    
    .. note::
       Esta función es puramente informativa y no altera el estado del juego.
    """

    # Creamos variable sala y le asignamos el valor estado.ubicacion que viene de estado.py
    sala = estado.ubicacion

    # Le pedimos a mundo.py la descripción de la sala actual y la guardamos en texto_sala
    texto_sala = mundo.descripcion_sala(sala)

    # Pedimos la lista de objetos que hay en la sala actual
    objetos = mundo.objetos_visibles(sala)

    # Unimos los elementos de la lista objetos, si hay uno queda igual, si son varios los separa con coma.
    if objetos:
        texto_objetos = ", ".join(objetos)
    else:
        texto_objetos = "(No hay objetos en esta sala, mala suerte!)"

    # Pedimos a mundo.py las salidas disponibles desde la sala actual.
    salidas = mundo.salidas_disponibles(sala)

    # salidas es un diccionario en mundo.py con claves (n,s...) y sus valores correspondientes (pasillo, armas...)
    if salidas:
        texto_salidas = ", ".join(salidas.keys())
    else:
        texto_salidas = "(No hay salidas, espabila y búscala)"

    # Devolvemos el texto final uniendo descripcion de la sala (texto_sala), objetos (texto_objetos) y las salidas (texto_salidas)
    return (
        texto_sala
        + "\n\nObjetos visibles: " + texto_objetos
        + "\nSalidas: " + texto_salidas
    )


def mover(direccion: str) -> str:
    """
    Ejecuta el desplazamiento del jugador hacia una nueva sala.

    Valida la entrada del usuario, verifica la existencia de una conexión 
    en el mapa y actualiza la ubicación en el estado global. 
    Lanza excepciones ante entradas no válidas.

    :param direccion: El punto cardinal o comando de dirección (n, s, e, o).
    :type direccion: str
    :return: El resultado de invocar a `mirar()` en la nueva sala o mensaje de error.
    :rtype: str
    :raises ValueError: Si la dirección está vacía, es inválida (no es n/s/e/o),
                    o no existe salida en esa dirección desde la sala actual.
    """

    # Si el usuario no puso direccion.
    if not direccion:
        raise ValueError("Debe haber una dirección. Usa n/s/e/o, no tenemos todo el día.")

    # Nos quedamos con la primera letra (por si escriben 'norte')
    # Convertimos el primer carácter del texto a minúscula, aceptamos "N","n","norte", "Norte".
    d = direccion[0].lower()

    # Comprobamos que sea una dirección válida
    if d not in ("n", "s", "e", "o"):
        raise ValueError("Dirección incorrecta. Debes usar n/s/e/o. A este ritmo no saldrás nunca")

    # Guardamos en sala_actual dónde está el jugador ahora mismo (viene de estado.py)
    sala_actual = estado.ubicacion

    # Pedimos a mundo.py el diccionario de SALIDAS de esa sala.
    salidas = mundo.salidas_disponibles(sala_actual)

    # Si la letra no está en el diccionario de SALIDAS (mundo.py), no hay camino.
    if d not in salidas:
        # No movemos al jugador, solo mostramos el mensaje.
        return "No puedes ir en esa dirección, estas perdido en el laberinto."

    # Si la salida existe, buscamos en el diccionario a que sala vamos.
    sala_destino = salidas[d]

    # Cambiamos la ubicacion del jugador, actualizando el estado en estado.py
    estado.ubicacion = sala_destino

    # Añadimos la sala destino al conjunto de salas visitadas (estado.visitadas)
    estado.visitadas.add(sala_destino)

    # Llamamos a mirar() para generar el texto de la nueva sala y lo devolvemos para que juego.py lo imprima.
    return mirar()


def mapa() -> str:
    """
    Genera una representación visual simplificada del progreso del jugador.

    Itera sobre la estructura de datos del mapa para identificar la posición 
    relativa del usuario y las áreas ya exploradas.

    :return: Un mapa en formato ASCII con la leyenda de estado.
    :rtype: str

    .. note::
       Esta función no modifica el estado del juego y es útil para la 
       orientación del jugador dentro del laberinto.
    """
    texto = "MAPA (X=tú, V=visitada, -=no visitada)\n"

    # Recorre cada fila del mapa.
    for fila in mundo.MAPA:
        # Recorre cada sala de esa fila:
        # - si es donde estás pone X
        # - si ya la visitaste pone V
        # - si no pone -
        for sala_id in fila:
            if sala_id == estado.ubicacion:
                texto += "X "
            elif sala_id in estado.visitadas:
                texto += "V "
            else:
                texto += "- "
        texto += "\n"

    return texto
