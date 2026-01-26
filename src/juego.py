
# Lógica principal del juego

"""
juego.py — Bucle principal + parser de comandos
===============================================

Responsabilidad:
- Implementar el bucle de entrada/salida por consola.
- Parsear la línea del usuario y delegar la acción al módulo correcto.
- Mostrar mensajes (descripciones, errores, ayuda).

Relaciones:
- Importa: `estado` (para leer/escribir ubicacion, inventario, visitadas...),
           `mundo` (para describir habitaciones, objetos visibles, conexiones),
           `movimiento` (para comandos de moverse),
           `acciones` (para coger/soltar/inspeccionar/usar).
- No contiene datos del mundo ni reglas de acciones; solo coordina.

Interfaz pública:
- `iniciar() -> None`: imprime bienvenida, primer "mirar" y entra en el bucle.
- `interpretar(linea: str) -> str | None`: convierte la línea en comando/args y delega.

Comandos mínimos (Reto 1):
- Movimiento: `n s e o` y `ir <dir>`
- `mirar`, `inventario`, `coger <obj>`, `soltar <obj>`, `inspeccionar <obj>`
- `ayuda, `salir`
- `usar ...` delega a `acciones.usar`. En Reto 1 puede lanzar `NotImplementedError`.

Validación/Errores (UT05):
- Capturar `ValueError` (entradas inválidas, objetos inexistentes).
- Capturar `NotImplementedError` (acciones aún no implementadas en Reto 1).
- Mensajes amigables (sin stacktrace).

Notas futuras:
- Reto 2: mostrar salud/resumen de estado si hace falta.
- Reto 3: imprimir resultados de encuentros/eventos que gestione otro módulo.
"""

import estado
import movimiento
import acciones

AYUDA = """\
Comandos:
  n s e o        Moverse (norte/sur/este/oeste)
  ir <dir>       Igual que moverse
  mirar          Describir la sala actual
  inventario     Ver inventario
  coger <obj>    Recoger objeto
  soltar <obj>   Soltar objeto
  inspeccionar <obj>
  usar <obj> [en <dest>]   (Reto 2)
  mapa           Ver el mapa
  ayuda          Esta ayuda
  salir          Terminar
"""

def interpretar(linea: str) -> str | None:
    t = linea.strip().split()
    if not t:
        return ""
    cmd, *args = t
    cmd = cmd.lower()

    if cmd in ("n", "s", "e", "o"):
        return movimiento.mover(cmd)
    if cmd == "ir" and args:
        return movimiento.mover(args[0])
    if cmd == "ir":
        return "Te falta la dirección. Ejemplo: ir n"
    if cmd == "mirar":
        return movimiento.mirar()
    if cmd == "inventario":
        return acciones.inventario_str()
    if cmd == "coger" and args:
        return acciones.coger(" ".join(args))
    if cmd == "soltar" and args:
        return acciones.soltar(" ".join(args))
    if cmd == "inspeccionar" and args:
        return acciones.inspeccionar(" ".join(args))
    if cmd == "usar" and args:
        obj = args[0]
        destino = args[2] if len(args) >= 3 and args[1] == "en" else None
        return acciones.usar(obj, destino)
    if cmd == "mapa":
        return movimiento.mapa_str()
    if cmd == "ayuda":
        return AYUDA
    if cmd == "salir":
        return "__EXIT__"
    return "No entiendo ese comando. Escribe 'ayuda' para ver opciones."

def iniciar() -> None:
    print("Bienvenid@ al Laberinto de Texto (Reto 1). Escribe 'ayuda' para ver comandos.\n")
    print(movimiento.mirar())

    while True:
        try:
            linea = input("\n> ")
        except (EOFError, KeyboardInterrupt):
            print("\nInterrumpido.")
            break

        if not linea.strip():
            continue

        try:
            resp = interpretar(linea)
        except NotImplementedError as e:
            print(f"[Aún no disponible] {e}")
            continue
        except ValueError as e:
            print(f"[Entrada no válida] {e}")
            continue
        except Exception as e:
            # No mostrar stacktrace en clase; mensaje claro
            print(f"[Error inesperado] {e}")
            continue

        if resp == "__EXIT__":
            print("¡Hasta pronto!")
            break
        if resp:
            print(resp)
            if estado.victoria:
                print("\n🏆 ¡Has escapado del laberinto!")
                break
if __name__ == "__main__":
    iniciar()

