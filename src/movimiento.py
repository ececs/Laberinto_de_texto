
"""
movimiento.py — Movimiento N/S/E/O y utilidades de mapa
=======================================================

Responsabilidad:
- Mover al jugador entre salas válidas.
- Validar direcciones y existencia de salida.
- Devolver la descripción de la nueva sala (o mensaje claro si no se puede).

Relaciones:
- Importa: `estado` para leer/modificar `ubicacion` y `visitadas`.
- Importa: `mundo` para consultar `SALIDAS` y descripción de sala.
- No importa `juego` ni `acciones`.

Funciones sugeridas:
- `mover(dir_: str) -> str`: intenta mover; si no hay salida, devuelve texto “No puedes ir…”.
- `mirar() -> str`: devuelve descripción + objetos visibles + salidas.
- `mapa_ascii() -> str`: genera el mapa según `mundo.COORDS` y las `estado.visitadas`.

Reto 1:
- Implementar `mover`, `mirar`, `mapa_ascii`.
- Validación: si `dir_` no es {n,s,e,o} → ValueError (UT05).

Reto 2:
- Podéis impedir movimiento si ciertas condiciones no se cumplen (ej., oscuridad sin antorcha encendida), pero manteniendo mensajes claros.

Reto 3:
- (Opcional) penalizaciones o eventos al entrar en salas concretas (aunque lo ideal es mantenerlo en `acciones` para no mezclar responsabilidades).
"""


"""
mundo.py — Datos del laberinto
- Sin lógica de juego; solo estructuras y funciones de consulta.
- Debe cubrir Reto 1: 8–10 habitaciones, 3–5 objetos, coords para mapa.
"""

from typing import Dict, List, Tuple

import estado
import mundo

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


def mirar() -> str:
    """Devuelve descripción, objetos visibles y salidas de la sala actual."""
    desc = mundo.descripcion_sala(estado.ubicacion)
    objs = mundo.objetos_visibles(estado.ubicacion)
    exits = mundo.salidas_disponibles(estado.ubicacion)
    objs_txt = ", ".join(objs) if objs else "(ninguno)"
    exits_txt = ", ".join(exits.keys()) if exits else "(ninguna)"
    return f"{desc}\n\nObjetos visibles: {objs_txt}\nSalidas: {exits_txt}"


def mover(dir_: str) -> str:
    """Mueve al jugador en la dirección indicada (n/s/e/o) y devuelve la descripción de la nueva sala."""
    if not dir_:
        raise ValueError("Dirección vacía.")
    d = dir_[0].lower()
    if d not in ("n", "s", "e", "o"):
        raise ValueError("Dirección inválida. Usa n/s/e/o.")
    salidas = mundo.salidas_disponibles(estado.ubicacion)
    destino = salidas.get(d)
    if not destino:
        return "No puedes ir en esa dirección."
    estado.ubicacion = destino
    estado.visitadas.add(destino)
    return mirar()


def mapa_ascii() -> str:
    """Mapa minimalista: lista salas con marca P (player), V (visitada) o ."""
    lines = []
    for sala in sorted(mundo.COORDS.keys()):
        mark = "P" if sala == estado.ubicacion else ("V" if sala in estado.visitadas else ".")
        lines.append(f"{mark} {sala}")
    return "\n".join(lines)
