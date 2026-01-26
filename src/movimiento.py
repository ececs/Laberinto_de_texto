"""
movimiento.py
=============
Este módulo se encarga de:
- Mostrar información de la sala actual con el comando mirar.
- Mover al jugador por el laberinto con los comandos n/s/e/o.
- Mostrar un mapa simple.

Usa:
- estado.py para leer/modificar la ubicación del jugador.
- mundo.py para consultar datos del laberinto como salidas, descripciones y objetos.
"""

import estado
import mundo


def mirar():
    """
    Construye y devuelve un texto con información de la sala actual:
    1 - Describiendo la sala.
    2 - Objetos que hay en el suelo.
    3 - Direcciones por las que puede salir.
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


def mover(direccion):
    """
    Intenta mover al jugador en una dirección:
    - Si la dirección es inválida -> ValueError (juego.py lo captura)
    - Si no hay salida -> mensaje claro
    - Si hay salida -> cambia estado.ubicacion y devuelve mirar()
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
        return "No puedes ir en esa dirección, se te complica la cosa."

    # Si la salida existe, buscamos en el diccionario a que sala vamos.
    sala_destino = salidas[d]

    # Cambiamos la ubicacion del jugador, actualizando el estado en estado.py
    estado.ubicacion = sala_destino

    # Añadimos la sala destino al conjunto de salas visitadas (estado.visitadas)
    estado.visitadas.add(sala_destino)

    # Llamamos a mirar() para generar el texto de la nueva sala y lo devolvemos para que juego.py lo imprima.
    return mirar()


def mapa_str():
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
