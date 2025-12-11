import random

#MENÚ DEL JUEGO

# Selecciona una palabra aleatoria.
# Inicializa la lista de letras adivinadas.
# Muestra el progreso y el dibujo según los fallos.
# Recibe entrada del usuario.
# Valida la letra (una sola, no repetida, alfabética).
# Actualiza el estado con programación funcional.
# Comprueba si el jugador gana o pierde.

# Funciones puras del juego

def elegir_palabra(palabras):
    """Devuelve una palabra aleatoria."""
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    """
    Construye la palabra mostrando letras adivinadas y guiones.
    Ejemplo: p _ o g r _ m a c i ó n
    """
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def calcular_fallos(palabra, letras_adivinadas):
    """Cuenta cuántas letras incorrectas ha dicho el jugador."""
    return len([l for l in letras_adivinadas if l not in palabra])

def ha_ganado(palabra, letras_adivinadas):
    """Verifica si todas las letras de la palabra han sido adivinadas."""
    return all(letra in letras_adivinadas for letra in palabra)

def obtener_dibujo_ahorcado(fallos):
    """Devuelve la etapa del ahorcado según los fallos."""
    dibujos = [
        """
          +---+
              |
              |
              |
            =====
        """,
        """
          +---+
          O   |
              |
              |
            =====
        """,
        """
          +---+
          O   |
          |   |
              |
            =====
        """,
        """
          +---+
          O   |
         /|   |
              |
            =====
        """,
        """
          +---+
          O   |
         /|/  |
              |
            =====
        """,
        """
          +---+
          O   |
         /|/  |
         /    |
            =====
        """,
        """
          +---+
          O   |
         /|/  |
         / /  |
            =====
        """
    ]
    return dibujos[min(fallos, 6)]

# Lógica principal del juego

def jugar_ahorcado():
    palabras = ["nelly", "maceta", "hipopotamo", "teclado", "pantalla", "casa", "programacion"]

    palabra = elegir_palabra(palabras)
    letras_adivinadas = []
    max_fallos = 6

    print(" ¡Bienvenidos a mi juego del Ahorcado!")
    print("Adivina la palabra secreta. Tienes 6 vidas.\n")

    while True:
        fallos = calcular_fallos(palabra, letras_adivinadas)

        print(obtener_dibujo_ahorcado(fallos))
        print("Palabra:", mostrar_progreso(palabra, letras_adivinadas))
        print("Letras usadas:", " ".join(letras_adivinadas) if letras_adivinadas else "(ninguna)")
        print("Intentos restantes:", max_fallos - fallos)

        # Si sale Ganador
        if ha_ganado(palabra, letras_adivinadas):
            print("\n ¡Felicidades! Adivinaste la palabra:", palabra.upper())
            break

        # Si sale Perdedor
        if fallos >= max_fallos:
            print("\n ¡Perdedor! La palabra era:", palabra.upper())
            break

        # Entrada del usuario
        letra = input("\nIngresa una letra: ").lower().strip()

        if len(letra) != 1 or not letra.isalpha():
            print(" Ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas:
            print(" Ya usaste esa letra.")
            continue

        # Agregar letra
        letras_adivinadas.append(letra)

# Ejecutar el juego

jugar_ahorcado()

