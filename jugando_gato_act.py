import random

# Funciones puras

def crear_tablero():
    """
    Crea un tablero vacío de 3x3.

    Returns:
        list[list[str]]: Matriz 3x3 con espacios en blanco.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def tablero_actualizado(tablero, fila, col, jugador):
    """
    Devuelve un nuevo tablero con la jugada aplicada,
    sin modificar el tablero original (inmutabilidad).

    Args:
        tablero (list[list[str]]): Tablero actual.
        fila (int): Fila donde se coloca la ficha.
        col  (int): Columna donde se coloca la ficha.
        jugador (str): Símbolo del jugador ("X" u "O").

    Returns:
        list[list[str]]: Nuevo tablero modificado.
    """
    return [
        [
            jugador if (r == fila and c == col) else tablero[r][c]
            for c in range(3)
        ]
        for r in range(3)
    ]

def casillas_libres(tablero):
    """
    Obtiene todas las casillas vacías del tablero.

    Args:
        tablero (list[list[str]]): Tablero actual.

    Returns:
        list[tuple[int,int]]: Lista de coordenadas libres.
    """
    return [
        (r, c)
        for r in range(3)
        for c in range(3)
        if tablero[r][c] == " "
    ]


def hay_ganador(tablero, jugador):
    """
    Verifica si un jugador ganó el juego evaluando:
    - 3 filas
    - 3 columnas
    - 2 diagonales

    Args:
        tablero (list[list[str]]): Tablero actual.
        jugador (str): Símbolo del jugador.

    Returns:
        bool: True si el jugador ganó, False en caso contrario.
    """
    lineas = [
        # Filas
        [tablero[r][0], tablero[r][1], tablero[r][2]] for r in range(3)
    ] + [
        # Columnas
        [tablero[0][c], tablero[1][c], tablero[2][c]] for c in range(3)
    ] + [
        # Diagonales
        [tablero[0][0], tablero[1][1], tablero[2][2]],
        [tablero[0][2], tablero[1][1], tablero[2][0]]
    ]

    return any(all(c == jugador for c in linea) for linea in lineas)


def empate(tablero):
    """
    Determina si el tablero está lleno sin ganador.

    Args:
        tablero (list[list[str]]): Tablero actual.

    Returns:
        bool: True si hay empate, False si aún hay espacios.
    """
    return all(tablero[r][c] != " " for r in range(3) for c in range(3))


def jugada_computadora(tablero):
    """
    Selecciona aleatoriamente una casilla libre para la computadora.

    Args:
        tablero (list[list[str]]): Tablero actual.

    Returns:
        tuple[int,int]: Coordinadas (fila, columna) elegidas.
    """
    return random.choice(casillas_libres(tablero))

# Funciones con interacción (entrada / salida)

def mostrar_tablero(tablero):
    """
    Muestra el tablero en consola en formato visual.

    Args:
        tablero (list[list[str]]): Tablero actual.

    Side Effects:
        Imprime en pantalla.
    """
    print("\n  0 1 2")
    for i, fila in enumerate(tablero):
        print(i, fila[0], fila[1], fila[2])


def turno_jugador(tablero, jugador):
    """
    Solicita al usuario una jugada válida y devuelve un
    tablero actualizado sin mutar el original.

    Args:
        tablero (list[list[str]]): Estado actual.
        jugador (str): "X"

    Returns:
        list[list[str]]: Tablero tras la jugada válida.
    """
    while True:
        entrada = input("\nTu jugada (formato fila,columna): ")

        if "," not in entrada:
            print("❗ Usa el formato fila,columna — Ejemplo: 1,2")
            continue

        fila, col = entrada.split(",")

        if not fila.isdigit() or not col.isdigit():
            print("❗ Debes escribir números.")
            continue

        fila, col = int(fila), int(col)

        if fila not in range(3) or col not in range(3):
            print("❗ Coordenadas fuera del tablero.")
            continue

        if tablero[fila][col] != " ":
            print("❗ Esa casilla está ocupada.")
            continue

        return tablero_actualizado(tablero, fila, col, jugador)

def turno_pc(tablero, pc):
    """
    Ejecuta un turno de la computadora y devuelve
    un tablero actualizado.

    Args:
        tablero (list[list[str]]): Estado actual.
        pc (str): "O"

    Returns:
        list[list[str]]: Tablero actualizado.
    """
    print("\nLa computadora está pensando...")
    fila, col = jugada_computadora(tablero)
    return tablero_actualizado(tablero, fila, col, pc)


# Controlador principal del juego

def jugar():
    """
    Controlador del juego usando un enfoque funcional:
    - Sin estados globales
    - Cada acción genera un nuevo tablero
    - Interacciones separadas de la lógica pura

    Side Effects:
        Imprime y solicita datos del usuario.
    """
    jugador = "X"
    pc = "O"

    tablero = crear_tablero()

    print("JUEGO DEL GATO")
    print("Tú juegas con X | La computadora juega con O")

    mostrar_tablero(tablero)

    while True:
        # Turno del jugador
        tablero = turno_jugador(tablero, jugador)
        mostrar_tablero(tablero)

        if hay_ganador(tablero, jugador):
            print("\n🎉 ¡Ganaste!")
            break

        if empate(tablero):
            print("\n🤝 ¡Empate!")
            break

        # Turno de la computadora
        tablero = turno_pc(tablero, pc)
        mostrar_tablero(tablero)

        if hay_ganador(tablero, pc):
            print("\n💻 La computadora gana.")
            break

        if empate(tablero):
            print("\n🤝 ¡Empate!")
            break


# Ejecutar el juego
jugar()
