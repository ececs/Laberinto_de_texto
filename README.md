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

¿QUE ARCHIVOS USA EL JUEGO Y PARA QUÉ SIRVE CADA UNO?

juego.py = el “cerebro” que habla con el jugador
Pide texto por consola (input)
Decide qué comando has escrito
Llama a otras funciones (mover, coger, etc.)
Imprime respuestas y controla cuándo termina el juego 
Funciones clave:
interpretar(linea): convierte lo que escribes en acciones (parser).
iniciar(): el bucle principal del juego.

estado.py = la “memoria” del juego
Aquí se guardan variables que cambian durante la partida: 
ubicacion: en qué sala estás (empieza en "entrada")
inventario: lista de objetos que llevas
visitadas: set (conjunto) de salas por las que ya pasaste
victoria: si has ganado o no
(preparado para futuro) salud y flags
Funciones:
resetear(): reinicia todo como al empezar.
vivo(): devuelve True si salud > 0 (Reto 2+).
estado_resumen(): texto para ver el estado.

mundo.py = el mapa y los datos del laberinto
Aquí NO hay “reglas”, solo datos: habitaciones, salidas, objetos. 
Usa diccionarios como:
HABITACIONES: id -> {nombre, descripcion}
SALIDAS: id -> { "n": "otraSala", ... }
OBJETOS_EN_SALA: id -> ["llave", "antorcha", ...]
COORDS: id -> (x,y) para el mapa ASCII
Y funciones “de consulta”:
descripcion_sala(sala_id)
objetos_visibles(sala_id)
salidas_disponibles(sala_id)
coord_sala(sala_id)

movimiento.py = moverse y mirar
Tu archivo movimiento.py (ojo: en lo que me aparece cargado hay código mezclado, parece que pegaste funciones de movimiento dentro de ese archivo) tiene estas funciones usadas por juego.py: 
mover(dir_): cambia estado.ubicacion si existe salida
mirar(): describe sala + objetos visibles + salidas
mapa_ascii(): muestra un listado tipo mapa con P/V/ . (Jugador/Visitada/No visitada)

acciones.py = inventario y acciones sobre objetos
Funciones usadas por juego.py: 
coger(obj)
soltar(obj)
inventario_str()
inspeccionar(obj)
usar(obj, destino) (en Reto 1 lanza NotImplementedError si lo tienes)