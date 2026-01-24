"""
movimiento.py
=============
Aquí está la lógica de movimiento y de "mirar".

- No pedimos input() aquí.
- No hacemos prints aquí (solo devolvemos textos).
- juego.py imprime lo que devolvemos.

Usa:
- estado.py: guarda la sala actual (estado.ubicacion) y salas visitadas (estado.visitadas)
- mundo.py: datos del laberinto (descripciones, salidas, objetos, coords)
"""

import estado
import mundo


def mirar():
    """
    Devuelve un texto con:
    - descripción de la sala actual
    - objetos visibles
    - salidas disponibles
    """

    sala = estado.ubicacion  # sala donde está el jugador

    # 1) Descripción
    texto_sala = mundo.descripcion_sala(sala)

    # 2) Objetos visibles
    objetos = mundo.objetos_visibles(sala)
    if objetos:
        texto_objetos = ", ".join(objetos)
    else:
        texto_objetos = "(ninguno)"

    # 3) Salidas disponibles
    salidas = mundo.salidas_disponibles(sala)
    if salidas:
        texto_salidas = ", ".join(salidas.keys())  # por ejemplo: n, s, e, o
    else:
        texto_salidas = "(ninguna)"

    # Devolvemos el texto final
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

    # Si el usuario no puso nada
    if not direccion:
        raise ValueError("Dirección vacía. Usa n/s/e/o.")

    # Nos quedamos con la primera letra (por si escriben 'norte')
    d = direccion[0].lower()

    # Comprobamos que sea una dirección válida
    if d not in ("n", "s", "e", "o"):
        raise ValueError("Dirección inválida. Usa n/s/e/o.")

    sala_actual = estado.ubicacion
    salidas = mundo.salidas_disponibles(sala_actual)

    # Si no existe salida en esa dirección
    if d not in salidas:
        return "No puedes ir en esa dirección."

    # Si existe salida, nos movemos
    sala_destino = salidas[d]
    estado.ubicacion = sala_destino

    # Marcamos la sala como visitada
    estado.visitadas.add(sala_destino)

    # Mostramos la nueva sala
    return mirar()


def mapa_ascii():
    """
    Mapa simple (lista de salas):
    - P = jugador aquí
    - V = sala visitada
    - . = sala no visitada
    """

    lineas = []

    # sorted(...) ordena para que siempre salga igual (built-in)
    for sala in sorted(mundo.COORDS.keys()):
        if sala == estado.ubicacion:
            marca = "P"
        elif sala in estado.visitadas:
            marca = "V"
        else:
            marca = "."

        lineas.append(marca + " " + sala)

    return "\n".join(lineas)
