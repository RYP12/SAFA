# Ejercicio 1: Pinta el número mayor
def ejercicio1(num1, num2, num3):
    mayor = max(num1, num2, num3)
    print(f"El número más grande es: {mayor}")


# Ejercicio 2: Las palabras de más de 8 letras
def ejercicio2(palabra):
    if palabra and len(palabra) >= 8:
        print(palabra)


# EXTRA: Modifica el ejercicio para que se le pueda indicar como parámetro el número mínimo de vocales
def ejercicio2_extra(palabra, min_vocales):
    if palabra and len(palabra) >= 8:
        cuenta_vocales = sum(1 for char in palabra if char.lower() in "aeiou")
        if cuenta_vocales >= min_vocales:
            print(palabra)


# Ejercicio 3: La más grande y la más pequeña
def ejercicio3(palabra1, palabra2, palabra3, palabra4):
    palabras = [palabra1, palabra2, palabra3, palabra4]
    mayor = max(palabras, key=len)
    menor = min(palabras, key=len)
    print(f"La palabra más grande es: {mayor}")
    print(f"La palabra más pequeña es: {menor}")


# EXTRA: Modifica el ejercicio para que se le puedan pasar todas las palabras que queramos
def ejercicio3_extra(*palabras):
    mayor = max(palabras, key=len)
    menor = min(palabras, key=len)
    print(f"La palabra más grande es: {mayor}")
    print(f"La palabra más pequeña es: {menor}")


# Ejercicio 4: Los divisores del último
def ejercicio4(num1, num2, num3, num4, num5):
    numeros = [num1, num2, num3, num4, num5]
    ultimo = numeros[-1]
    divisores = [num for num in numeros[:-1] if num % ultimo == 0]
    print(f"Los números que se pueden dividir por {ultimo} son: {divisores}")


# EXTRA: Modifica el ejercicio para que se le pueda pasar todos los números que queramos
def ejercicio4_extra(*numeros):
    ultimo = numeros[-1]
    divisores = [num for num in numeros[:-1] if num % ultimo == 0]
    print(f"Los números que se pueden dividir por {ultimo} son: {divisores}")


# Ejercicio 5: Las de más de 3 vocales
def ejercicio5(palabra1, palabra2, palabra3):
    palabras = [palabra1, palabra2, palabra3]
    for palabra in palabras:
        if sum(1 for char in palabra if char.lower() in "aeiou") > 3:
            print(palabra)


# EXTRA: Modifica el ejercicio para que se le pueda pasar el número de palabras que queramos
def ejercicio5_extra(*palabras):
    for palabra in palabras:
        if sum(1 for char in palabra if char.lower() in "aeiou") > 3:
            print(palabra)


# Ejercicio 6: Descriptor de palabras
def ejercicio6(palabra):
    if palabra:
        print("La palabra es distinta de \"\"")
    else:
        print("La palabra es \"\"")

    if len(palabra) > 5:
        print("La palabra tiene más de 5 letras")
    else:
        print("La palabra no tiene más de 5 letras")

    if any(char.lower() in "aeiou" for char in palabra):
        print("La palabra tiene vocales.")
    else:
        print("La palabra no tiene vocales.")

    if any(char.lower() not in "aeiou" and char.isalpha() for char in palabra):
        print("La palabra tiene consonantes.")
    else:
        print("La palabra no tiene consonantes.")

    if any(char in "áéíóúÁÉÍÓÚ" for char in palabra):
        print("La palabra tiene vocales acentuadas.")
    else:
        print("La palabra no tiene vocales acentuadas.")

    print(f"La palabra tiene {len(palabra)} letras.")


# Ejemplos de llamadas a las funciones
ejercicio1(10, 20, 15)
ejercicio2("programacion")
ejercicio2_extra("programacion", 3)
ejercicio3("casa", "edificio", "murcielago", "auto")
ejercicio3_extra("casa", "edificio", "murcielago", "auto", "arbol")
ejercicio4(10, 20, 30, 40, 5)
ejercicio4_extra(10, 20, 30, 40, 5, 50, 60)
ejercicio5("elefante", "rinoceronte", "gato")
ejercicio5_extra("elefante", "rinoceronte", "gato", "murciélago")
ejercicio6("Lápiz")
ejercicio6("")
ejercicio6("aeiouaeiou")
