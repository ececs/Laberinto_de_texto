
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
  mapa           Ver el mapa
  reiniciar      Reinicia la partida desde el inicio
  ayuda          Esta ayuda
  salir          Terminar
"""

def interpretar(linea):
    """
    Interpreta el comando introducido por el usuario y ejecuta la acción correspondiente.
    Devuelve el mensaje de respuesta o None.
    """
    # Dividimos la línea en una lista de palabras
    palabras = linea.strip().split()
    
    # Si no hay palabras, devolvemos cadena vacía
    if not palabras:
        return ""
    
    # Almacena la primera palabra como el comando y el resto como argumentos
    comando = palabras[0].lower()
    argumentos = palabras[1:]
    
    # Si el comando es una dirección (n, s, e, o), llamamos a mover
    if comando in ("n", "s", "e", "o"):
        return movimiento.mover(comando)
    
    # Si el comando es "ir" con dirección (n, s, e, o), llamamaos a mover con 
    # la dirección asignada, si no hay dirección, mensaje de error
    if comando == "ir":
        if argumentos:
            return movimiento.mover(argumentos[0])
        else:
            return "Te falta la dirección. Ejemplo: ir n"
    

    # Muestra el mapa con las salas visitadas si el comando es "mapa"
    if comando == "mapa":
        if argumentos:
            return "El comando 'mapa' no necesita argumentos."
        return movimiento.mapa_str()
    
    # Si el comando es "reiniciar", reinicia ubicación, inventario, visitadas y victoria.
    # Finalmente muestra la sala inicial otra vez.
    if comando == "reiniciar":
        estado.resetear()
        return movimiento.mirar()
    
    # Si el comando es "mirar", llamamos a mirar
    if comando == "mirar":
        return movimiento.mirar()
    
    # Si el comando es "inventario", llamamos a inventario_str
    if comando == "inventario":
        return acciones.inventario_str()

    if comando == "coger" and argumentos:
        return acciones.coger(" ".join(argumentos))
    if comando == "soltar" and argumentos:
        return acciones.soltar(" ".join(argumentos))
    if comando == "inspeccionar" and argumentos:
        return acciones.inspeccionar(" ".join(argumentos))

    if comando == "ayuda":
        return AYUDA
    
    # Si el comando es "salir", terminamos el juego
    if comando == "salir":
        return "__EXIT__"
    
    # Si no reconocemos el comando
    return "No entiendo ese comando. Escribe 'ayuda' para ver opciones."


def iniciar():
    """Función principal que inicia el juego y gestiona el bucle principal."""
    # Mensaje de bienvenida
    print("Bienvenido al Laberinto de Texto. Escribe 'ayuda' para ver comandos.\n")
    
    # Mostramos la primera sala, llamando a mirar()
    estado.visitadas.add(estado.ubicacion) # Para que sala inicial cuente como visitada
    print(movimiento.mirar())
    
    # Bucle principal del juego
    while True:
        try:
            # Solicitamos comando al usuario
            linea = input("\n> ")
        except (EOFError, KeyboardInterrupt):
            # Si el usuario pulsa Ctrl+C o Ctrl+D
            print("\nInterrumpido.")
            break
        
        # Si la línea está vacía, solicitamos otro comando
        if not linea.strip():
            continue
        
        try:
            # Interpretamos el comando
            respuesta = interpretar(linea)
        except NotImplementedError as error:
            # Funcionalidad aún no implementada
            print(f"[Aún no disponible] {error}")
            continue
        except ValueError as error:
            # Entrada no válida (por ejemplo, datos incorrectos)
            print(f"[Entrada no válida] {error}")
            continue
        except Exception as error:
            # Cualquier otro error inesperado
            print(f"[Error inesperado] {error}")
            continue
        
        # Si el usuario escribió "salir", terminamos el juego
        if respuesta == "__EXIT__":
            print("¡Hasta pronto!")
            break
        
        # Mostramos la respuesta si existe
        if respuesta:
            print(respuesta)
        
        # Comprobamos si el jugador ha ganado, y salimos del bucle
        if estado.victoria:
            print("\n¡Has escapado del laberinto!")
            break


# Este if comprueba si el archivo se ejecuta directamente
# Si es así, arranca el juego
if __name__ == "__main__":
    iniciar()
