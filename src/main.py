"""
LABERINTO DE TEXTO - Proyecto 9
Desarrollo de Aplicaciones Web (DAW)
Curso 2025-2026

RETO 1: Implementación Básica

Integrantes del equipo:
- Persona 1: [Nombre] - Sistema de Habitaciones y Navegación
- Persona 2: [Nombre] - Sistema de Inventario
- Persona 3: [Nombre] - Parser de Comandos y Lógica Principal

Descripción:
Un juego de aventura textual donde el jugador debe navegar por un
laberinto de 9 habitaciones, recoger objetos clave y encontrar la
salida.

Funcionalidades implementadas:
✅ 9 habitaciones interconectadas
✅ Navegación en 4 direcciones (N, S, E, O)
✅ Sistema de inventario (máximo 5 objetos)
✅ Mapa de habitaciones visitadas
✅ Manejo de excepciones para inventario
✅ Sistema de comandos flexible
"""

"""
main.py — Punto de entrada del programa
======================================

Responsabilidad:
- Orquestar el arranque del juego.
- Configurar (opcional) el entorno o argumentos CLI.
- Invocar a `juego.iniciar()` y no contener lógica del juego.

Relaciones:
- Importa solo `juego`.
- No importa `acciones`, `movimiento`, `mundo` ni `estado` directamente para evitar acoplamiento.

Flujo esperado:
1) Validación breve de entorno (opcional).
2) Llamada a `juego.iniciar()`.

Reto 1:
- Simplemente arrancar el bucle del juego.

Reto 2:
- Sin cambios aquí; la lógica nueva se añade en otros módulos.

Reto 3:
- Sin cambios aquí; seguirá siendo el punto de entrada.

Convenciones:
- Mantener este archivo mínimo y legible para la corrección.
"""



"""
main.py — Punto de entrada del programa
Patrón A: `juego` es un MÓDULO que expone la función `iniciar()`.

Responsabilidad:
- Arrancar el juego y capturar errores generales sin mostrar tracebacks
  (limpio para la presentación en clase).
- NO contiene lógica de juego.

Ejecución recomendada (desde la raíz del proyecto):
    python3 -m src.main
"""

import juego

def main():
    """Función principal para iniciar el juego."""
    try:
        # Llamamos a la función iniciar() del módulo juego
        juego.iniciar()
        # Si no se lanzan ninguna excepcion y finaliza el juego, 
        # mostramos el mensaje de despedida
        print("\nGracias por jugar a Laberinto de Texto.")
    except KeyboardInterrupt:
        # Si el usuario pulsa Ctrl+C, salimos sin error
        print("\n¡Hasta pronto!")
    except Exception as error:
        # Capturamos cualquier error para que el programa no se cierre bruscamente
        print(f"\nError: {error}")
        print("El juego se cerrará.")

# Comprobamos si el archivo se ejecuta directamente (python main.py)
# Si es así, __name__ vale "__main__" y se ejecuta main()
# Si el archivo se importa desde otro, no se ejecuta automáticamente
if __name__ == "__main__":
    main()