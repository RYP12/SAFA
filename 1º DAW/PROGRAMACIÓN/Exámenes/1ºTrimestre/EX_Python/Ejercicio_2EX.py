#EJERCICIO 2
import random
lista_palabras = ["puerto", "barco", "copa", "mandos"]

palabra_aleatorio = (random.choice(lista_palabras))

palabra_desordenada = []

while len(palabra_desordenada) != len(palabra_aleatorio):

    for palabra in palabra_aleatorio,:
        letra_aleatoria = (random.choice(palabra_aleatorio))
        if not letra_aleatoria in palabra_desordenada:
            palabra_desordenada.append(letra_aleatoria)



vidas = 3
palabras_citadas = []


while vidas > 0:
    print("---------------------------------------------------------------------------")
    print(f"Vidas : {vidas}")
    print(f"Palabras citadas: {palabras_citadas}")
    print(f"Palabra: {' '.join(palabra_desordenada)}")
    print("---------------------------------------------------------------------------")
    palabra_in = input("Ordena la palabra: ").lower()

    if palabra_in in palabras_citadas:
        print("Ya has dicho esa palabra. Intenta con otra.")
        continue

    palabras_citadas.append(palabra_in)

    if palabra_in == palabra_aleatorio:
        print("¡Felicidades! Has adivinado la palabra.")
        break
    else:
        vidas -= 1

if vidas == 0:
    print("Lo siento, has perdido. La palabra era:", palabra_aleatorio)




