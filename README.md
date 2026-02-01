# Laberinto de Texto - Proyecto UT04/UT05

¡Buenas! Este es nuestro proyecto para el módulo de Programación. Lo hemos desarrollado entre **Pablo Diaz, Rodrigo Sanmartin y Eudaldo Cal**. Es una aventura conversacional por consola donde tienes que ir moviéndote por un laberinto.

Lo hemos montado todo de forma modular para que cada parte del código se encargue de una cosa, siguiendo lo que hemos visto en clase sobre el ámbito de las variables y el control de errores.

## 📄 Documentación técnica (Sphinx)
Hemos generado la documentación con Sphinx para que se vean bien todas las funciones que hemos programado, los parámetros que reciben y lo que devuelven. Podéis verla aquí:

👉 **[Enlace a la web de documentación](https://ececs.github.io/Laberinto_de_texto/)**

---

## 🏗️ Cómo está organizado el código
Nos hemos repartido el trabajo en varios módulos para que el proyecto sea más limpio y fácil de seguir:

* **main.py**: Es el punto de entrada. Llama al inicio y tiene el `try-except` para que el programa no pete si hay un error raro.
* **juego.py**: Aquí está el bucle principal y el `parser` de comandos que interpreta lo que escribe el usuario.
* **mundo.py**: Contiene todos los datos (diccionarios de habitaciones, objetos y las salidas de cada sala).
* **estado.py**: Gestiona las variables globales (inventario, salud, ubicación actual) para que no se pierdan durante la partida.
* **movimiento.py**: Toda la lógica de navegación y la descripción del mapa por el que nos movemos.
* **acciones.py**: La interacción con los objetos, como cogerlos de la sala, soltarlos o inspeccionarlos.

## 🛠️ Retos implementados
1. **Reto 1 (Laberinto)**: Hemos diseñado unas 10 habitaciones conectadas con sus descripciones.

## 📋 Requisitos de la unidad
* **UT04**: Usamos la palabra clave `global` en el módulo de estado para gestionar el inventario desde cualquier función.
* **UT05**: Hemos metido control de excepciones con `ValueError` para direcciones que no existen y `NotImplementedError` para funciones que están planteadas pero no activas.