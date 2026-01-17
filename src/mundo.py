
"""
mundo.py — Definición del mundo (habitaciones, salidas, objetos)
================================================================

Responsabilidad:
- Declarar la estructura del laberinto:
    * HABITACIONES: dict id -> {nombre, descripcion}
    * SALIDAS: dict id -> dict(dir -> id)
    * OBJETOS_EN_SALA: dict id -> [objetos]
    * COORDS: dict id -> (x, y) para dibujar mapa ASCII
- Proveer funciones utilitarias de consulta de datos (no de lógica).

Relaciones:
- No importa `estado` ni `acciones`. Debe ser un módulo "de datos".
- `juego` y `acciones` leen de aquí para describir y verificar.

Funciones sugeridas:
- `descripcion_sala(sala_id: str) -> str`
- `objetos_visibles(sala_id: str) -> list[str]`
- `salidas_disponibles(sala_id: str) -> dict[str, str]`
- `coord_sala(sala_id: str) -> tuple[int, int]`

Reto 1:
- Debe contener 8–10 habitaciones, 3–5 objetos, y coords razonables para el mapa.
- Descripciones con pistas suaves (sin lógica de puzle aún).

Reto 2:
- Añadir textos con pistas contextuales (p. ej., mención de puerta, cofre, olor a gas, etc.).

Reto 3:
- Anotar qué salas pueden tener encuentros aleatorios (p. ej., metadatos como `encuentros_prob: 0.2` si queréis).
"""


"""
mundo.py — Datos del laberinto
- Sin lógica de juego; solo estructuras y funciones de consulta.
- Debe cubrir Reto 1: 8–10 habitaciones, 3–5 objetos, coords para mapa.
"""

from typing import Dict, List, Tuple

# Coordenadas (x, y) para mapa ASCII
COORDS: Dict[str, Tuple[int, int]] = {
    "entrada":     (0, 0),
    "pasillo":     (0, 1),
    "armas":       (1, 1),
    "biblioteca":  (-1, 1),
    "cripta":      (-1, 2),
    "pozo":        (0, 2),
    "puente":      (1, 2),
    "tesoreria":   (1, 3),
    "salida":      (0, 3),
}

HABITACIONES: Dict[str, Dict[str, str]] = {
    "entrada":    {"nombre": "Entrada del Laberinto", "descripcion": "Una antorcha parpadea. Al norte, un pasillo angosto."},
    "pasillo":    {"nombre": "Pasillo", "descripcion": "Paredes con marcas antiguas. Este y oeste parecen transitables."},
    "armas":      {"nombre": "Sala de Armas", "descripcion": "Estantes corroídos; algo brilla bajo una mesa."},
    "biblioteca": {"nombre": "Biblioteca", "descripcion": "Estantes polvorientos y olor a pergamino húmedo."},
    "cripta":     {"nombre": "Cripta", "descripcion": "Frío intenso. Susurros que no sabes si imaginarios."},
    "pozo":       {"nombre": "Pozo", "descripcion": "Se oye agua. Hacia el norte parece haber claridad."},
    "puente":     {"nombre": "Puente", "descripcion": "Puente de piedra sobre un abismo."},
    "tesoreria":  {"nombre": "Tesorería", "descripcion": "Cofres y tapices. (Interacciones en Reto 2)"},
    "salida":     {"nombre": "Puerta de Salida", "descripcion": "Una gran puerta. (Mecánica de salida en Reto 2/3)"},
}

# Conexiones N/S/E/O
SALIDAS: Dict[str, Dict[str, str]] = {
    "entrada":    {"n": "pasillo"},
    "pasillo":    {"s": "entrada", "e": "armas", "w": "biblioteca", "n": "pozo"},
    "armas":      {"w": "pasillo", "n": "puente"},
    "biblioteca": {"e": "pasillo", "n": "cripta"},
    "cripta":     {"s": "biblioteca"},
    "pozo":       {"s": "pasillo", "n": "salida"},
    "puente":     {"s": "armas", "n": "tesoreria"},
    "tesoreria":  {"s": "puente"},
    "salida":     {"s": "pozo"},
}

# Objetos por sala (3–5 total para Reto 1)
OBJETOS_EN_SALA: Dict[str, List[str]] = {
    "armas": ["llave"],
    "biblioteca": ["pergamino"],
    "cripta": ["medallon"],
    "pozo": ["antorcha"],
    # otras salas sin objetos
    "entrada": [], "pasillo": [], "puente": [], "tesoreria": [], "salida": [],
}

# ---- Funciones utilitarias (sin lógica) ----

def descripcion_sala(sala_id: str) -> str:
    meta = HABITACIONES.get(sala_id, {})
    nombre = meta.get("nombre", sala_id)
    desc = meta.get("descripcion", "")
    return f"== {nombre} ==\n{desc}"

def objetos_visibles(sala_id: str) -> list[str]:
    return list(OBJETOS_EN_SALA.get(sala_id, []))

def salidas_disponibles(sala_id: str) -> dict[str, str]:
    return dict(SALIDAS.get(sala_id, {}))

def coord_sala(sala_id: str) -> tuple[int, int]:
    return COORDS.get(sala_id, (0, 0))
