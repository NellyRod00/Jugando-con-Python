# Crear el tablero vacío
# Mostrar el tablero vacío
# Mostrar tablero
# Verificar si el jugador gana
# Buscar espacios libres
# Verificar si la computadora gana

import random

# Crear el tablero vacío
tablero = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

jugador = "X"
computadora = "O"
jugadas = 0
ganador = None

print("Juego del GATO")
print("Tú eres X y la computadora es O")
print("Ingresa tu jugada como fila,columna (por ejemplo: 1,2)\n")

# Mostrar el tablero vacío
print("  0 1 2")
print("0", tablero[0][0], tablero[0][1], tablero[0][2])
print("1", tablero[1][0], tablero[1][1], tablero[1][2])
print("2", tablero[2][0], tablero[2][1], tablero[2][2])

while True:
    # --- TURNO DEL JUGADOR ---
    while True:
        entrada = input("\nTu turno (X): ")

        if "," not in entrada:
            print("⚠️ Usa el formato fila,columna (ejemplo: 1,2)")
            continue

        partes = entrada.split(",")
        if len(partes) != 2:
            print("Ingresa solo dos números.")
            continue

        if not partes[0].isdigit() or not partes[1].isdigit():
            print("Debes escribir números.")
            continue

        fila = int(partes[0])
        columna = int(partes[1])

        if fila < 0 or fila > 2 or columna < 0 or columna > 2:
            print("Posición fuera del tablero.")
            continue

        if tablero[fila][columna] != " ":
            print("Esa casilla ya está ocupada.")
            continue

        tablero[fila][columna] = jugador
        jugadas = jugadas + 1
        break

    print("\n  0 1 2")
    for i in range(3):
        print(i, tablero[i][0], tablero[i][1], tablero[i][2])

    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            ganador = jugador
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            ganador = jugador

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        ganador = jugador
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        ganador = jugador

    if ganador == jugador:
        print("\n ¡Ganaste! Eres el mejor jugador de Gato.")
        break

    if jugadas == 9:
        print("\n ¡Empate!")
        break

    # --- TURNO DE LA COMPUTADORA ---
    print("\nTurno de la computadora...")

    casillas_libres = []
    for f in range(3):
        for c in range(3):
            if tablero[f][c] == " ":
                casillas_libres.append((f, c))

    jugada_pc = random.choice(casillas_libres)
    fila_pc = jugada_pc[0]
    columna_pc = jugada_pc[1]

    tablero[fila_pc][columna_pc] = computadora
    jugadas = jugadas + 1

    print("\n  0 1 2")
    for i in range(3):
        print(i, tablero[i][0], tablero[i][1], tablero[i][2])

    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == computadora:
            ganador = computadora
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == computadora:
            ganador = computadora

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == computadora:
        ganador = computadora
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == computadora:
        ganador = computadora

    if ganador == computadora:
        print("\n💻 La computadora gana. ¡Sigue practicando!")
        break

    if jugadas == 9:
        print("\n🤝 ¡Empate!")
        break
