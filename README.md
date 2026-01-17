# Laberinto_de_texto
Navegación por habitaciones usando comandos de dirección (norte, sur, este,
oeste). Aprenderás sobre el ámbito de variables y gestión de inventarios complejos.
Contenidos UT04
Ámbito de variables (scope) para gestionar el inventario del jugador en
diferentes "habitaciones" implementadas como funciones.
Contenidos UT05
Control de excepciones cuando el usuario intenta usar un objeto que no está
en su inventario o realizar una acción no implementada
(NotImplementedError).
"Cada habitación es un desafío, cada decisión cuenta. ¡Encuentra la salida!"
OBLIGATORIO
Reto 1: Diseño de Laberinto Simplificado
Diseña un laberinto con 8-10 habitaciones interconectadas, cada una con descripciones y salidas en 4 direcciones básicas (N, S, E,
O). Implementa un sistema de inventario básico para 3-5 objetos clave y un mapa simple que muestre las habitaciones visitadas.
Reto 2: Lógica de Interacción Simplificada
Añade elementos interactivos básicos en cada habitación (puertas con llave, cofres simples). Implementa un sistema de salud
simple (3-5 puntos de vida) y descripciones de habitaciones con pistas. Se elimina la funcionalidad de guardar/cargar.
Reto 3: Sistema de Encuentros Básico
Desarrolla un sistema para encuentros simples con enemigos (sin sistema de combate complejo) y un inventario de objetos
básicos (sin estadísticas de personaje). Añade eventos aleatorihos simples y una habitación final con un desafío.
Guía de Desarrollo
Pasos para Resolver el Proyecto
1.
Diseñar habitaciones: Crea diccionario con descripciones y
salidas
2.
Conectar habitaciones: Define qué habitación conecta con cuál
(N, S, E, O)
Posición del jugador: Mantén registro de habitación actual3.
4.
Parser de comandos: Interpreta entrada del jugador (ir norte,
examinar, etc.)
Sistema de inventario: Permite recoger y usar objetos5.
6.
Eventos y puzzles: Implementa interacciones especiales por
habitación
Condiciones de salida: Define cómo se completa el laberinto7.