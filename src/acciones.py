
"""
acciones.py — Acciones del jugador sobre el mundo (coger, soltar, inspeccionar, usar…)
=======================================================================================

Responsabilidad:
- Implementar la lógica de acciones sobre inventario y entorno.
- NO pintar el bucle ni pedir input (eso es tarea de `juego`).

Relaciones:
- Importa: `estado` para leer/modificar inventario, ubicacion, salud, visitadas, flags.
- Importa: `mundo` para validar si un objeto está en la sala, etc.
- No debe importar `juego` (evitar dependencia circular).

Funciones sugeridas (Reto 1):
- `coger(obj: str) -> str`: mueve obj de sala al inventario; si no está, ValueError.
- `soltar(obj: str) -> str`: del inventario a la sala; si no lo tienes, ValueError.
- `inventario_str() -> str`: devuelve cadena formateada con el inventario actual.
- `inspeccionar(obj: str) -> str`: descripción breve de objetos conocidos.
- `usar(obj: str, destino: str | None = None) -> str`:
    * Reto 1: si obj no está en inventario -> ValueError (UT05).
    * Reto 1: lanzar `NotImplementedError` para posponer la interacción a Reto 2.

Reto 2 (extensión aquí):
- Implementar interacciones reales:
    * `usar antorcha` -> estado.antorcha_encendida = True
    * `usar llave en puerta` en sala de salida -> estado.victoria = True
    * cofre en tesorería, etc.
- Aplicar cambios a `estado.salud` por trampas/eventos (si se define aquí o en un módulo aparte).

Reto 3:
- Disparar encuentros simples (probabilidad) y resolver efectos mínimos (perder 1 punto de salud, retroceder de sala, etc.).
- Mantener la complejidad baja: sin sistema de combate completo.
"""


"""
acciones.py — Lógica de acciones del jugador
- No pide input ni pinta bucles. Devuelve siempre textos claros.
- En Reto 1, `usar` lanza NotImplementedError (UT05) si el objeto está en inventario.
"""

import estado
import mundo
# Diccionario que guarda descripción corta de cada objeto. 
# Cuando el jugador escribe inspeccionar llave, devuelve un texto.
OBJ_DESCS = {
    "llave": "Una llave pequeña y vieja, parece estar muy oxidada.",
    "pergamino": "Un pergamino con símbolos borrosos, puede que sirva de algo.",
    "medallon": "Un medallón frío al tacto, si fuera de oro no estaría rallado.",
    "antorcha": "Podría encenderse, pero hace falta fuego.",
}
# Función coger. Mira en que sala estas, pide a mundo.py la lista de objetos visibles de la sala. 
# Si no está, devuelve mensaje.
def coger(obj: str) -> str:
    objs = mundo.objetos_visibles(estado.ubicacion)
    if obj not in objs:
        return f"No hay '{obj}' aquí."
# Si está, lo quita de la sala(remove) y lo mete en inventario(append).
    mundo.OBJETOS_EN_SALA[estado.ubicacion].remove(obj)
    estado.inventario.append(obj)
# Finalmente devuelve texto de confirmación.
    return f"Has cogido '{obj}'."

# Función soltar.Comprueba si el objeto está en inventario.
# Si no lo tienes, devuelve un mensaje.
def soltar(obj: str) -> str:
    if obj not in estado.inventario:
        return f"No tienes '{obj}'."
# Si lo tienes lo quita del inventario(remove).
# Lo añade en la sala actual(append).
# Devuelve confirmación.
    estado.inventario.remove(obj)
    mundo.OBJETOS_EN_SALA[estado.ubicacion].append(obj)
    return f"Has soltado '{obj}'."

# Función inventario. Si tiene cosas, las une con comas, si está vacio, lo muestra.
def inventario_str() -> str:
    return "Inventario: " + (", ".join(estado.inventario) if estado.inventario else "(vacío)")

# Función inspeccionar objetos.
# Comprueba si el objeto está en tu inventario o visible en la sala actual.
# Si está devuelve descripción, si no frase genérica.
# Si el objeto no está ni en inventario ni en sala, devuelve "No ves"
def inspeccionar(obj: str) -> str:
    if obj in estado.inventario or obj in mundo.objetos_visibles(estado.ubicacion):
        return OBJ_DESCS.get(obj, f"No ves nada especial en '{obj}'.")
    return f"No ves '{obj}'."

