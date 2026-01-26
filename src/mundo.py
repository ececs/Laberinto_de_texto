"""
mundo.py
========
Este archivo guarda los datos del laberinto.

Contiene diccionarios con:
- Habitaciones (nombre y descripción)
- Salidas (n/s/e/o, es decir, a qué sala vas)
- Objetos que hay en cada sala.

Aquí solo devolvemos la información para que otros archivos la usen.
"""

# -----------------------------
# 2) Habitaciones (texto)
# -----------------------------
# Guardamos nombre y descripción de cada sala.
HABITACIONES = {  # Diccionario con todas las salas: clave = id de la sala, valor = nombre y descripción.
    "entrada": {
        "nombre": "Entrada al Laberinto",
        "descripcion": "Una antorcha parpadea. Al norte, un pasillo largo y oscuro."
    },
    "pasillo": {
        "nombre": "Pasillo",
        "descripcion": "Las paredes son antiguas de piedra desgastada, no puedes ver mucho, pero este (e) y oeste (o) parecen transitables."
    },
    "armas": {
        "nombre": "Sala de Guardia",
        "descripcion": "Restos de armaduras y escudos oxidados, si alguien salió de aquí, fue hace mucho. Puedes volver al oeste (o) o continuar por el norte (n)."
    },
    "biblioteca": {
        "nombre": "Biblioteca",
        "descripcion": "Estantes polvorientos y libros desgastados. Hay sillas y mesas viejas, y además un olor a pergamino húmedo."
    },
    "cripta": {
        "nombre": "Cripta",
        "descripcion": "Hay un silencio aterrador y frío intenso. Se oyen susurros, pero no sabes si son imaginarios."
    },
    "pozo": {
        "nombre": "Pozo",
        "descripcion": "Se oye agua. Hacia el norte (n) parece haber claridad."
    },
    "puente": {
        "nombre": "Puente",
        "descripcion": "Puente de piedra sobre un abismo, no parece verse el final de la caída."
    },
    "tesoreria": {
        "nombre": "Tesorería",
        "descripcion": "Cofres de madera reforzada, monedas esparcidas y copas doradas cubiertas de telarañas. Quizá haya algo útil entre tanto polvo."
    },
    "salida": {
        "nombre": "Puerta de Salida",
        "descripcion": "Una gran puerta se alza frente a ti. El aire es más fresco aquí, pero algo te dice que aún no eres libre."
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
    datos = HABITACIONES.get(sala_id, {})  # Buscamos la sala. Si no existe, usamos {} para no dar error.
    nombre = datos.get("nombre", sala_id)  # Usamos sala_id por si falta "nombre", así tiene más robustez.
    descripcion = datos.get("descripcion", "")  # Si falta "descripcion", ponemos cadena vacía (más robusto).
    return "== " + nombre + " ==\n" + descripcion  # Devolvemos texto final con formato y salto de línea.


def objetos_visibles(sala_id):
    """
    Devuelve una lista con los objetos que hay en una sala.
    """
    return list(OBJETOS_EN_SALA.get(sala_id, []))  # Devuelve objetos de la sala. list() hace copia para consultar sin tocar el original.


def salidas_disponibles(sala_id):
    """
    Devuelve un diccionario con las salidas de la sala.
    """
    return dict(SALIDAS.get(sala_id, {}))  # Devuelve las salidas. dict() hace copia para no modificar el original.

# Mapa simple 3x3: cada celda tiene el id de la sala (string)
MAPA = [
    ["tesoreria", "salida", "puente"],
    ["cripta",    "pozo",   "armas"],
    ["biblioteca","pasillo","entrada"],
]
