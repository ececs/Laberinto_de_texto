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

from juego import juego

def main():
    """Funcion principal para iniciar el juego."""
    try:
        juego = juego()
        juego.iniciar()
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        print("El juego se cerrará.")
        print("Gracias por jugar a Laberinto de Texto.")

if __name__ == "__main__":
    main()