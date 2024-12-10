def juego_ahorcado(palabra):
    vidas = 5
    letras_citadas = []
    palabra_oculta = ['_'] * len(palabra)

    while vidas > 0:
        print("---------------------------------------------------------------------------")
        print(f"Vidas : {vidas}")
        print(f"Letras citadas: {letras_citadas}")
        print(f"Palabra: {' '.join(palabra_oculta)}")
        print("---------------------------------------------------------------------------")
        letra = input("Dime una letra: ").lower()

        if letra in letras_citadas:
            print("Ya has dicho esa letra. Intenta con otra.")
            continue

        letras_citadas.append(letra)

        if letra in palabra:
            print("Has acertado")
            for i, char in enumerate(palabra):
                if char == letra:
                    palabra_oculta[i] = letra
        else:
            vidas -= 1

        if '_' not in palabra_oculta:
            print("¡Felicidades! Has adivinado la palabra.")
            break

    if vidas == 0:
        print("Lo siento, has perdido. La palabra era:", palabra)

# Ejemplo de uso
juego_ahorcado("patinete")
