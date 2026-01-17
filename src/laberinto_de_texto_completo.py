# LABERINTO DE TEXTO (SIMPLE) — UT04 + UT05
# - Habitaciones como funciones
# - Inventario básico
# - Puerta con llave
# - Mapa simple (lista de visitadas)
# - Excepciones: KeyError, ValueError, NotImplementedError

DIRECCIONES = {"n": "n", "s": "s", "e": "e", "o": "o",
              "norte": "n", "sur": "s", "este": "e", "oeste": "o"}

def normalizar(txt: str) -> str:
    return txt.strip().lower()

def ayuda():
    print("Comandos:")
    print("  n/s/e/o  | ir <norte/sur/este/oeste>")
    print("  mirar    | inventario")
    print("  coger <objeto> | usar <objeto>")
    print("  salir")

def mostrar_inventario(inv, visitadas, vida):
    print(f"Vida: {vida}/5")
    if inv:
        print("Inventario:", ", ".join(sorted(inv)))
    else:
        print("Inventario: (vacío)")
    print("Visitadas:", " -> ".join(visitadas))

def parsear_comando(entrada: str):
    cmd = normalizar(entrada)
    if not cmd:
        raise ValueError("Comando vacío.")

    # Direcciones directas
    if cmd in ("n", "s", "e", "o"):
        return ("mover", cmd)

    # "ir norte"
    partes = cmd.split()
    if partes[0] == "ir" and len(partes) >= 2:
        d = partes[1]
        if d not in DIRECCIONES:
            raise ValueError("Dirección inválida.")
        return ("mover", DIRECCIONES[d])

    if cmd == "mirar":
        return ("mirar", None)
    if cmd == "inventario":
        return ("inventario", None)
    if cmd == "ayuda":
        return ("ayuda", None)
    if cmd == "salir":
        return ("salir", None)

    if partes[0] == "coger" and len(partes) >= 2:
        return ("coger", " ".join(partes[1:]))

    if partes[0] == "usar" and len(partes) >= 2:
        return ("usar", " ".join(partes[1:]))

    # UT05: acción no implementada
    raise NotImplementedError("Acción no implementada. Escribe 'ayuda'.")

def main():
    # ===== UT04 (Scope) =====
    # Variables del juego viven aquí (ámbito envolvente)
    vida = 5
    inventario = set()
    visitadas = ["ENTRADA"]

    # Objetos "en el suelo" por habitación (simple)
    suelo = {
        "ALMACEN": {"llave"},
        "BIBLIOTECA": {"mapa"},
        "LABORATORIO": {"pocion"},
    }

    # Estado de puerta (bloqueo de salida)
    puerta_abierta = False

    # ===== Habitaciones como FUNCIONES (UT04) =====
    def entrada():
        nonlocal vida
        print("\n== ENTRADA ==")
        print("Estás en la entrada del laberinto. Hay un pasillo al este y un almacén al sur.")
        return {"e": pasillo, "s": almacen}

    def pasillo():
        print("\n== PASILLO ==")
        print("Un pasillo largo. Al norte hay una biblioteca. Al este, una galería. Al oeste, la entrada.")
        return {"w": entrada, "n": biblioteca, "e": galeria}

    def almacen():
        print("\n== ALMACÉN ==")
        print("Cajas viejas. Quizá haya algo útil aquí. Al norte vuelves a la entrada.")
        return {"n": entrada}

    def biblioteca():
        print("\n== BIBLIOTECA ==")
        print("Libros polvorientos. Hay una salida al sur (pasillo).")
        return {"s": pasillo}

    def galeria():
        print("\n== GALERÍA ==")
        print("Una galería fría. Al norte hay un laboratorio. Al oeste vuelves al pasillo. Al este hay una cámara.")
        return {"w": pasillo, "n": laboratorio, "e": camara}

    def laboratorio():
        print("\n== LABORATORIO ==")
        print("Frascos y polvo. Al sur vuelves a la galería.")
        return {"s": galeria}

    def camara():
        print("\n== CÁMARA ==")
        print("Una cámara con una puerta al este (parece cerrada). Al oeste vuelves a la galería.")
        return {"w": galeria, "e": salida}

    def salida():
        print("\n== SALIDA ==")
        print("Ves la luz al otro lado...")
        return {}

    # Habitación actual (función)
    habitacion_actual = entrada

    def describir_objetos(hab_nombre):
        objs = suelo.get(hab_nombre, set())
        if objs:
            print("Ves en el suelo:", ", ".join(sorted(objs)))

    def nombre_habitacion(func_hab):
        # nombre "bonito" basado en el nombre de la función
        return func_hab.__name__.upper()

    def coger_objeto(hab_nombre, obj):
        if obj not in suelo.get(hab_nombre, set()):
            raise ValueError(f"No veo '{obj}' aquí.")
        suelo[hab_nombre].remove(obj)
        inventario.add(obj)
        print(f"Has cogido: {obj}")

    def usar_objeto(hab_nombre, obj):
        nonlocal vida, puerta_abierta
        if obj not in inventario:
            # UT05: usar algo que no tienes
            raise KeyError(f"No tienes '{obj}' en tu inventario.")

        if obj == "pocion":
            if vida >= 5:
                print("Ya tienes la vida al máximo.")
                return
            vida = min(5, vida + 2)
            inventario.remove("pocion")
            print(f"Bebes la poción. Vida: {vida}/5")
            return

        if obj == "llave":
            if hab_nombre != "CAMARA":
                print("No hay ninguna puerta con cerradura aquí.")
                return
            puerta_abierta = True
            print("La llave encaja. ¡La puerta del este se ha desbloqueado!")
            return

        # UT05: objeto sin comportamiento implementado
        raise NotImplementedError(f"El objeto '{obj}' no tiene uso implementado.")

    # ===== Bucle principal =====
    print("LABERINTO DE TEXTO (SIMPLE). Objetivo: llegar a la SALIDA.")
    ayuda()

    while True:
        if vida <= 0:
            print("Te has quedado sin vida. Game Over.")
            break

        hab_nombre = nombre_habitacion(habitacion_actual)
        salidas = habitacion_actual()  # Ejecuta la función-habitación
        describir_objetos(hab_nombre)

        entrada_usuario = input("\n> ")

        try:
            accion, dato = parsear_comando(entrada_usuario)

            if accion == "salir":
                print("Saliendo del juego.")
                break

            if accion == "ayuda":
                ayuda()
                continue

            if accion == "inventario":
                mostrar_inventario(inventario, visitadas, vida)
                continue

            if accion == "mirar":
                # Re-mostrar info básica (simple)
                print(f"Estás en {hab_nombre}. Salidas: {', '.join(sorted(salidas.keys()))}")
                describir_objetos(hab_nombre)
                continue

            if accion == "coger":
                coger_objeto(hab_nombre, dato)
                continue

            if accion == "usar":
                usar_objeto(hab_nombre, dato)
                continue

            if accion == "mover":
                d = dato
                if d not in salidas:
                    raise ValueError("No puedes ir por ahí.")

                siguiente = salidas[d]

                # Puerta bloqueada: CAMARA -> SALIDA por el este
                if hab_nombre == "CAMARA" and d == "e":
                    if not puerta_abierta:
                        raise PermissionError("La puerta está cerrada. Quizá una llave ayude.")

                habitacion_actual = siguiente
                nuevo_nombre = nombre_habitacion(habitacion_actual)
                if nuevo_nombre not in visitadas:
                    visitadas.append(nuevo_nombre)

                # Condición victoria
                if nuevo_nombre == "SALIDA":
                    print("\n¡HAS ESCAPADO! ¡Victoria!")
                    break

        except PermissionError as e:
            print(f"Acceso denegado: {e}")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
        except NotImplementedError as e:
            print(f"No implementado: {e}")

if __name__ == "__main__":
    main()
