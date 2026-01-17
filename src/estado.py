
"""
estado.py — Estado del juego (scope UT04)
=========================================

Responsabilidad:
- Almacenar y exponer el estado mutable del juego:
    * ubicacion: str
    * inventario: list[str]
    * visitadas: set[str]
    * salud: int (Reto 2+)
    * flags: dict[str, bool] (p.ej., "antorcha_encendida": False)
    * victoria: bool

Relaciones:
- No importa `mundo`, `acciones` ni `movimiento` (evitar ciclos).
- Es importado por otros módulos para leer/modificar el estado.

Interfaz sugerida:
- Variables de módulo (simples) + funciones utilitarias:
    * `resetear()` para iniciar partida.
    * `vivo() -> bool`: True si salud > 0 (Reto 2+).
    * `estado_resumen() -> str`: texto breve del estado (salud, inventario, flags).

Reto 1:
- `ubicacion = "entrada"`
- `inventario = []`
- `visitadas = set()`
- `victoria = False`
- (Salud y flags se pueden preparar pero no usar aún)

Reto 2:
- Añadir `salud = 5` y `flags = {"antorcha_encendida": False}`.
- Añadir helpers `daño(n)`, `curar(n)` si hace falta.

Reto 3:
- Mantener contadores sencillos para encuentros (para no dispararlos en cadena).
"""


"""
estado.py — Estado del juego (scope UT04)
- Solo variables y helpers simples. No importes otros módulos del dominio.
- Será importado por juego/acciones/movimiento.
"""

from typing import List, Set, Dict

# Reto 1 (mínimo)
ubicacion: str = "entrada"
inventario: List[str] = []
visitadas: Set[str] = set()
victoria: bool = False

# Preparado para Reto 2/3 (no usar aún si no queréis)
salud: int = 5                      # Reto 2
flags: Dict[str, bool] = {          # Reto 2
    "antorcha_encendida": False
}

def resetear() -> None:
    """Reinicia el estado a valores por defecto."""
    global ubicacion, inventario, visitadas, victoria, salud, flags
    ubicacion = "entrada"
    inventario = []
    visitadas = set()
    victoria = False
    salud = 5
    flags = {"antorcha_encendida": False}

def vivo() -> bool:
    """Reto 2+: True si salud > 0."""
    return salud > 0

def estado_resumen() -> str:
    """Texto breve del estado (para depuración/presentación)."""
    inv = ", ".join(inventario) if inventario else "(vacío)"
    return f"Ubicación: {ubicacion} | Salud: {salud} | Inventario: {inv}"
