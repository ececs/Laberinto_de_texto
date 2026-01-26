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

    sala = estado.ubicacion  # Creamos variable sala y le asignamos el valor estado.ubicacion que viene de estado.py

    texto_sala = mundo.descripcion_sala(sala) # Le pedimos a mundo.py la descripción de la sala actual y la guardamos en texto_sala

    objetos = mundo.objetos_visibles(sala) # Pedimos la lista de objetos que hay en la sala actual
    if objetos:
        texto_objetos = ", ".join(objetos) # Unimos los elementos de la lista objetos, si hay uno queda igual, si son varios los separa con coma.
    else:
        texto_objetos = "(No hay objetos en esta sala, mala suerte!)"

    
    salidas = mundo.salidas_disponibles(sala) # Pedimos a mundo.py las salidas disponibles desde la sala actual.
    if salidas:
        texto_salidas = ", ".join(salidas.keys())  # salidas es un diccionario en mundo.py con claves (n,s...) y  sus valores correspondientes (pasillo, armas...)
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
    d = direccion[0].lower() # Convertimos el primer carácter del texto a minúscula, aceptamos "N","n","norte", "Norte".

    # Comprobamos que sea una dirección válida
    if d not in ("n", "s", "e", "o"):
        raise ValueError("Dirección incorrecta. Debes usar n/s/e/o. A este ritmo no saldrás nunca")

    sala_actual = estado.ubicacion # Guardamos en sala_actual dónde está el jugador ahora mismo (viene de estado.py)
    salidas = mundo.salidas_disponibles(sala_actual) # Pedimos a mundo.py el diccionario de SALIDAS de esa sala.

    # Si no existe salida en esa dirección
    if d not in salidas: # Si la letra no está en el diccionario de SALIDAS (mundo.py), no hay camino.
        return "No puedes ir en esa dirección, se te complica la cosa." # No movemos al jugador, solo mostramos el mensaje.

    # Si existe salida, nos movemos
    sala_destino = salidas[d] # Si la salida existe, buscamos en el diccionario a que sala vamos.
    estado.ubicacion = sala_destino # Cambiamos la ubicacion del jugador, actualizando el estado en estado.py

    # Marcamos la sala como visitada
    estado.visitadas.add(sala_destino) # Añadimos la sala destino al conjunto de salas visitadas (estado.visitadas)

    return mirar() # Llamamos a mirar() para generar el texto de la nueva sala y lo devolvemos para que juego.py lo imprima.

def mapa_str():
    texto = "MAPA (X=tú, V=visitada, -=no visitada)\n"

    for fila in mundo.MAPA: #Recorre cada fila del mapa. Recorre cada sala de esa fila: si es donde estás pone X, si ya la visitaste pone V,si no pone -.
        for sala_id in fila:
            if sala_id == estado.ubicacion:
                texto += "X "
            elif sala_id in estado.visitadas:
                texto += "V "
            else:
                texto += "- "
        texto += "\n"

    return texto

