import random

# Palabras posibles
palabras = ["nelly", "maceta", "hipopotamo", "teclado", "pantalla", "casa", "programacion"]

# Selección aleatoria
palabra = random.choice(palabras)

# Variables
letras_adivinadas = []
intentos = 6  # cantidad total de vidas

# Dibujos del ahorcado (de menos a más fallos)
ahorcado = [
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
     /|\  |
          |
        =====
    """,
    """
      +---+
      O   |
     /|\  |
     /    |
        =====
    """,
    """
      +---+
      O   |
     /|\  |
     / \  |
        =====
    """
]

print("¡Bienvenido al juego del Ahorcado!")
print("Adivina la palabra secreta. Tienes", intentos, "intentos.\n")

while True:
    print(ahorcado[6 - intentos])

    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "

    print("Palabra:", palabra_mostrada.strip())
    print("Letras usadas:", " ".join(letras_adivinadas) if letras_adivinadas else "(ninguna)")
    print("Intentos restantes:", intentos)

    if all(letra in letras_adivinadas for letra in palabra):
        print("\n ¡Felicidades! Vaya!! Hasta que adivinaste:", palabra.upper())
        break

    letra = input("\nIngresa una letra: ").lower().strip()

    if len(letra) != 1 or not letra.isalpha():
        print(" Ingresa solo una letra válida.")
        continue

    if letra in letras_adivinadas:
        print(" Ya intentaste esa letra.")
        continue

    letras_adivinadas.append(letra)

    if letra in palabra:
        print(" ¡Muy Bien! La letra está en la palabra.")
    else:
        print(" La letra no está en la palabra.")
        intentos -= 1

    if intentos == 0:
        print(ahorcado[-1])
        print("\n ¡Perdedor jaja, suerte para la proxima! La palabra era:", palabra.upper())
        break
