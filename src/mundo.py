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
# Habitaciones (texto)
# -----------------------------
# Guardamos nombre y descripción de cada sala.
HABITACIONES = {  # Diccionario con todas las salas: clave = id de la sala, valor = nombre y descripción.
    "entrada": {
        "nombre": "Entrada al Laberinto",
        "descripcion": "Una antorcha parpadea. Al este (e), un pasillo largo y oscuro."
    },
    "pasillo": {
        "nombre": "Pasillo",
        "descripcion": "Las paredes son antiguas de piedra desgastada. Al oeste (o) está la entrada, al este (e) hay una biblioteca, y al sur (s) notas un aire frío."
    },
    "guardia": {
        "nombre": "Sala de Guardia",
        "descripcion": "Restos de armaduras y escudos oxidados. Al este (e) se abre una cripta, y al sur (s) hay un puente."
    },
    "biblioteca": {
        "nombre": "Biblioteca",
        "descripcion": "Estantes polvorientos y libros desgastados. Al oeste (o) vuelves al pasillo. Al sur (s) se oye agua."
    },
    "cripta": {
        "nombre": "Cripta",
        "descripcion": "Silencio aterrador y frío intenso. Al norte (n) regresas al pasillo, al oeste (o) está la guardia, al este (e) se oye agua, y al sur (s) hay una tesorería."
    },
    "pozo": {
        "nombre": "Pozo",
        "descripcion": "Se oye agua. Al norte (n) está la biblioteca, al oeste (o) la cripta y al sur (s) parece haber una salida."
    },
    "puente": {
        "nombre": "Puente",
        "descripcion": "Puente de piedra sobre un abismo. Al norte (n) vuelves a la sala de guardia y al este (e) hay una tesorería."
    },
    "tesoreria": {
        "nombre": "Tesorería",
        "descripcion": "Cofres reforzados, monedas y copas cubiertas de telarañas. Al norte (n) está la cripta, al oeste (o) el puente y al este (e) una gran puerta."
    },
    "salida": {
        "nombre": "Puerta de Salida",
        "descripcion": "Una gran puerta se alza frente a ti. Al norte (n) está el pozo y al oeste (o) la tesorería."
    },
}

# -----------------------------
# Salidas entre salas
# -----------------------------
# Para cada sala, indicamos a qué sala se llega con n/s/e/o.
SALIDAS = {
    "entrada":    {"e": "pasillo"},
    "pasillo":    {"o": "entrada", "e": "biblioteca", "s": "cripta"},
    "biblioteca": {"o": "pasillo", "s": "pozo"},
    "guardia":    {"e": "cripta", "s": "puente"},
    "cripta":     {"n": "pasillo", "o": "guardia", "e": "pozo", "s": "tesoreria" },
    "pozo":       {"n": "biblioteca", "o": "cripta" , "s": "salida"},
    "puente":     {"n": "guardia", "e": "tesoreria"},
    "tesoreria":  {"n": "cripta", "o": "puente", "e": "salida"},
    "salida":     {"n": "pozo", "o": "tesoreria"},
}

# -----------------------------
# Objetos por sala
# -----------------------------
# Lista de objetos que hay en cada sala al inicio.
OBJETOS_EN_SALA = {
    "entrada": ["antorcha"],
    "biblioteca": ["pergamino"],
    "cripta": ["medallon"],
    "pozo": ["llave"],

    # Salas sin objetos
    "guardia": [],
    "pasillo": [],
    "puente": [],
    "tesoreria": [],
    "salida": [],
}

# ------------------------------------------------
# Funciones de consulta (NO cambian el mundo)
# ------------------------------------------------

def descripcion_sala(sala_id):
    """
    Genera una cadena formateada con el título y descripción de una estancia.

    Utiliza el identificador de sala para acceder al diccionario global de 
    habitaciones, garantizando robustez mediante el uso de valores por defecto.

    :param sala_id: El identificador único de la sala a consultar.
    :type sala_id: str
    :return: Texto con formato para mostrar al usuario.
    :rtype: str
    """
    # Buscamos la sala. Si no existe, usamos {} para no dar error.
    datos = HABITACIONES.get(sala_id, {})

    # Usamos sala_id por si falta "nombre", así tiene más robustez.
    nombre = datos.get("nombre", sala_id)

    # Si falta "descripcion", ponemos cadena vacía (más robusto).
    descripcion = datos.get("descripcion", "")

    # Devolvemos texto final con formato y salto de línea.
    return "== " + nombre + " ==\n" + descripcion


def objetos_visibles(sala_id):
    """
    Retorna los ítems disponibles en una ubicación determinada.

    Se realiza una copia de la lista para asegurar que la consulta no afecte 
    accidentalmente a la estructura de datos original.

    :param sala_id: El identificador de la habitación actual.
    :type sala_id: str
    :return: Una lista con los nombres de los objetos encontrados.
    :rtype: list
    """
    # Devuelve objetos de la sala. list() hace copia para consultar sin tocar el original.
    return list(OBJETOS_EN_SALA.get(sala_id, []))


def salidas_disponibles(sala_id):
    """
    Recupera las rutas de navegación conectadas a una estancia.

    Permite identificar qué direcciones (n, s, e, o) son válidas desde la 
    posición actual.

    :param sala_id: Identificador de la estancia origen.
    :type sala_id: str
    :return: Diccionario de conexiones (dirección: sala_destino).
    :rtype: dict
    """
    # Devuelve las salidas. dict() hace copia para no modificar el original.
    return dict(SALIDAS.get(sala_id, {}))

# Mapa simple 3x3: cada celda tiene el id de la sala (string)
MAPA = [
    ["entrada", "pasillo", "biblioteca"],
    ["guardia",    "cripta",   "pozo"],
    ["puente","tesoreria","salida"],
]
