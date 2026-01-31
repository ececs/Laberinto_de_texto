"""
Módulo main.py

Punto de entrada principal para el proyecto Laberinto de Texto.

Este script actúa como el orquestador del arranque, encargándose de invocar 
el bucle principal del juego y gestionar las excepciones críticas de la 
aplicación para ofrecer una salida limpia al usuario.

Responsabilidad:
- Inicia el juego llamando a la función `iniciar()` del módulo `juego`.
- Captura y maneja excepciones globales para evitar trazas de error en la consola.
- Muestra mensajes de despedida o error según corresponda.

Relaciones:
- Importa: `juego` (para iniciar el bucle principal del juego).
Funciones principales:
- main(): función de entrada que configura el entorno de ejecución del juego.

"""

import juego

def main():
    """
    Función de entrada que configura el entorno de ejecución del juego.

    Se encarga de llamar a la lógica de inicio del módulo `juego` y captura 
    las interrupciones de teclado o errores inesperados para evitar que se 
    muestre el traceback de Python en la consola.

    :return: No devuelve ningún valor.
    :raises Exception: Captura errores genéricos durante la ejecución para informar al usuario.
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