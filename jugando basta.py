# Juego Basta con 3 categorías fijas y 3 rondas

letras = ["a", "b", "c"]

categorias = ["nombre", "apellido", "cosa"]

puntosTotales = 0

print("Bienvenido al juego Basta")
print("Tienes 3 rondas y 3 categorías: nombre, apellido, cosa")
print("Si quieres dejar una categoría vacía, solo presiona Enter")

ronda = 1
while ronda <= 3:
    letra = letras[ronda - 1]
    print("\n--- Ronda", ronda, "---")
    print("Letra de la ronda:", letra.upper())

    palabras = []
    for i in range(3):
        palabra = input("Escribe un " + categorias[i] + " que empiece con " + letra.upper() + ": ")
    
        palabras.append(palabra.capitalize())

    print("\nTus palabras:")
    for i in range(3):
        if palabras[i] == "":
            print(categorias[i] + ": (vacío)")
        else:
            print(categorias[i] + ": " + palabras[i])

    puntosRonda = 0
    for i in range(3):
        puntos = input("Puntos obtenidos en " + categorias[i] + ": ")
        if puntos.isdigit():
            puntosRonda += int(puntos)
        else:
            print("Se asigna 0 puntos")

    puntosTotales += puntosRonda
    print("Puntos de esta ronda:", puntosRonda)
    print("Puntos totales acumulados:", puntosTotales)

    ronda += 1

print("\n--- FIN DEL JUEGO ---")
print("Puntos totales:", puntosTotales)
print("¡Gracias por jugar!")
