"""
mundo.py
========
Este archivo guarda los datos del laberinto.

Contiene diccionarios con:
- Habitaciones (nombre y descripción)
- Salidas (n/s/e/o es decir a que sala vas)
- Objetos que hay en cada sala.

Aquí solo devolvemos la información para que otros archivos los usen.
"""

# -----------------------------
# 2) Habitaciones (texto)
# -----------------------------
# Guardamos nombre y descripción de cada sala.
HABITACIONES = {
    "entrada": {
        "nombre": "Entrada del Laberinto",
        "descripcion": "Una antorcha parpadea. Al norte, un pasillo angosto."
    },
    "pasillo": {
        "nombre": "Pasillo",
        "descripcion": "Paredes con marcas antiguas. Este y oeste parecen transitables."
    },
    "armas": {
        "nombre": "Sala de Armas",
        "descripcion": "Estantes corroídos; algo brilla bajo una mesa."
    },
    "biblioteca": {
        "nombre": "Biblioteca",
        "descripcion": "Estantes polvorientos y olor a pergamino húmedo."
    },
    "cripta": {
        "nombre": "Cripta",
        "descripcion": "Frío intenso. Susurros que no sabes si imaginarios."
    },
    "pozo": {
        "nombre": "Pozo",
        "descripcion": "Se oye agua. Hacia el norte parece haber claridad."
    },
    "puente": {
        "nombre": "Puente",
        "descripcion": "Puente de piedra sobre un abismo."
    },
    "tesoreria": {
        "nombre": "Tesorería",
        "descripcion": "Cofres y tapices. (Interacciones en Reto 2)"
    },
    "salida": {
        "nombre": "Puerta de Salida",
        "descripcion": "Una gran puerta. (Mecánica de salida en Reto 2/3)"
    },
}

# -----------------------------
# 3) Salidas entre salas
# -----------------------------
# Para cada sala, indicamos a qué sala se llega con n/s/e/o.
SALIDAS = {
    "entrada":    {"n": "pasillo"},
    "pasillo":    {"s": "entrada", "e": "armas", "o": "biblioteca", "n": "pozo"},
    "armas":      {"o": "pasillo", "n": "puente"},
    "biblioteca": {"e": "pasillo", "n": "cripta"},
    "cripta":     {"s": "biblioteca"},
    "pozo":       {"s": "pasillo", "n": "salida"},
    "puente":     {"s": "armas", "n": "tesoreria"},
    "tesoreria":  {"s": "puente"},
    "salida":     {"s": "pozo"},
}

# -----------------------------
# 4) Objetos por sala
# -----------------------------
# Lista de objetos que hay en cada sala al inicio.
OBJETOS_EN_SALA = {
    "armas": ["llave"],
    "biblioteca": ["pergamino"],
    "cripta": ["medallon"],
    "pozo": ["antorcha"],

    # Salas sin objetos
    "entrada": [],
    "pasillo": [],
    "puente": [],
    "tesoreria": [],
    "salida": [],
}

# ------------------------------------------------
# 5) Funciones de consulta (NO cambian el mundo)
# ------------------------------------------------

def descripcion_sala(sala_id):
    """
    Devuelve un texto con el nombre y la descripción de una sala.
    Si la sala no existe, devuelve algo básico para no romper el juego.
    """
    datos = HABITACIONES.get(sala_id, {})
    nombre = datos.get("nombre", sala_id)
    descripcion = datos.get("descripcion", "")
    return "== " + nombre + " ==\n" + descripcion


def objetos_visibles(sala_id):
    """
    Devuelve una lista con los objetos que hay en una sala.
    Devolvemos una COPIA de la lista para no modificarla sin querer.
    """
    return list(OBJETOS_EN_SALA.get(sala_id, []))


def salidas_disponibles(sala_id):
    """
    Devuelve un diccionario con las salidas de la sala.
    Devolvemos una COPIA para evitar modificaciones accidentales.
    """
    return dict(SALIDAS.get(sala_id, {}))

