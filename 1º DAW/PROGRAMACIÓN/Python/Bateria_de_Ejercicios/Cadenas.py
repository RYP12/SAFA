# Ejercicio 1
def ejercicio1():
    nombre = input("¿Cuál es tu nombre? ")
    print(f"Tu nombre es: {nombre}")


# Ejercicio 2
def ejercicio2(cadena):
    print(cadena.upper())


# Ejercicio 3
def ejercicio3(cadena):
    cuenta = cadena.lower().count('a')
    print(f"La letra 'a' aparece {cuenta} veces en la cadena.")


# Ejercicio 4
def ejercicio4(cadena):
    print(cadena[::-1])


# Ejercicio 5
def ejercicio5(cadena):
    print(cadena.replace(" ", ""))


# Ejercicio 6
def ejercicio6(cadena):
    vocales = "aeiouAEIOU"
    sin_vocales = ''.join([char for char in cadena if char not in vocales])
    print(sin_vocales)


# Ejercicio 7
def ejercicio7(cadena):
    palabras = cadena.split()
    print(f"La cadena contiene {len(palabras)} palabras.")


# Ejercicio 8
def ejercicio8(cadena):
    cadena_limpia = ''.join([char.lower() for char in cadena if char.isalnum()])
    es_palindromo = cadena_limpia == cadena_limpia[::-1]
    print(f"La cadena es un palíndromo: {es_palindromo}")


# Ejercicio 9
def ejercicio9(cadena, letra_vieja, letra_nueva):
    print(cadena.replace(letra_vieja, letra_nueva))


# Ejercicio 10
def ejercicio10(cadena):
    solo_alfabeticos = ''.join([char for char in cadena if char.isalpha() or char == " "])
    print(solo_alfabeticos)


# Ejercicio 11
def ejercicio11(lista_palabras):
    palabra_mas_larga = max(lista_palabras, key=len)
    print(f"La palabra más larga es: {palabra_mas_larga}")


# Ejercicio 12
def ejercicio12(cadena, palabra):
    cuenta = cadena.lower().split().count(palabra.lower())
    print(f"La palabra '{palabra}' aparece {cuenta} veces en la cadena.")


# Ejercicio 13
def ejercicio13(cadena):
    palabras = cadena.split()
    palabras.sort()
    print(' '.join(palabras))


# Ejercicio 14
def ejercicio14(cadena):
    reemplazos = str.maketrans("aeiou", "12345")
    print(cadena.translate(reemplazos))


# Ejercicio 15
def ejercicio15(cadena):
    def enmascarar_palabra(palabra):
        if len(palabra) > 2:
            return palabra[0] + '*' * (len(palabra) - 2) + palabra[-1]
        return palabra

    palabras = cadena.split()
    enmascaradas = [enmascarar_palabra(palabra) for palabra in palabras]
    print(' '.join(enmascaradas))


# Ejercicio 16
def ejercicio16(cadena):
    palabras = cadena.split()
    invertidas = [palabra[::-1] for palabra in palabras]
    print(' '.join(invertidas))


# Ejercicio 17
def ejercicio17(cadena):
    digitos = sum(char.isdigit() for char in cadena)
    print(f"La cadena contiene {digitos} dígitos.")


# Ejercicio 18
def ejercicio18(cadena):
    palabras = cadena.split()
    cuenta = sum(1 for palabra in palabras if len(palabra) >= 5)
    print(f"{cuenta} palabras tienen al menos 5 caracteres.")


# Ejercicio 19
def ejercicio19(cadena):
    palabras = cadena.split()
    print(' '.join(reversed(palabras)))


# Ejercicio 20
def ejercicio20(cadena):
    vocales = "aeiouAEIOU"
    solo_vocales = ''.join([char for char in cadena if char in vocales])
    print(solo_vocales)


# Ejercicio 21
def ejercicio21(cadena):
    palabras = cadena.split()
    capitalizadas = [palabra.capitalize() for palabra in palabras]
    print(' '.join(capitalizadas))


# Ejercicio 22
def ejercicio22(cadena, letra):
    cuenta = cadena.count(letra)
    print(f"La letra '{letra}' aparece {cuenta} veces en la cadena.")


# Ejercicio 23
def ejercicio23(cadena):
    sin_repetidas = ''.join(sorted(set(cadena), key=cadena.index))
    print(sin_repetidas)


# Ejercicio 24
def ejercicio24(cadena):
    palabras = cadena.split()
    palabras_ordenadas = sorted(palabras)
    print(' '.join(palabras_ordenadas))


# Ejercicio 25
def ejercicio25(cadena):
    palabras = cadena.split()
    resultado = ['*' * len(palabra) if len(palabra) >= 4 else palabra for palabra in palabras]
    print(' '.join(resultado))


# Ejercicio 26
def ejercicio26(cadena, palabra):
    cuenta = cadena.lower().split().count(palabra.lower())
    print(f"La palabra '{palabra}' aparece {cuenta} veces en la cadena.")


# Ejercicio 27
def ejercicio27(cadena):
    print(cadena.strip())


# Ejercicio 28
def ejercicio28(cadena):
    resultado = ''.join([char if i % 2 != 0 else 'X' for i, char in enumerate(cadena)])
    print(resultado)


# Ejercicio 29
def ejercicio29(cadena):
    desplazada = ''.join([chr(ord(
        char) + 1) if 'a' <= char <= 'y' or 'A' <= char <= 'Y' else 'a' if char == 'z' else 'A' if char == 'Z' else char
                          for char in cadena])
    print(desplazada)


# Ejercicio 30
def ejercicio30(cadena):
    palabras = cadena.split()
    palabras_inversas = reversed(palabras)
    print(' '.join(palabras_inversas))


# Llamada a las funciones de ejemplo
ejercicio1()  # Llamada que requiere entrada del usuario

# Llamada a funciones con ejemplos de cadena
ejercicio2("hola mundo")
ejercicio3("banana")
ejercicio4("hola")
ejercicio5("hola mundo")
ejercicio6("programacion")
ejercicio7("Esta es una prueba de contar palabras.")
ejercicio8("A man a plan a canal Panama")
ejercicio9("banana", "a", "o")
ejercicio10("hola@#mundo!!123")
ejercicio11(["manzana", "pera", "melocoton"])
ejercicio12("Hola hola mundo, hola a todos", "hola")
ejercicio13("Hola mundo esta es una prueba")
ejercicio14("aeiou")
ejercicio15("Hola mundo")
ejercicio16("Hola mundo")
ejercicio17("Hola1234")
ejercicio18("Hola mundo esta es una prueba con palabras largas")
ejercicio19("Hola mundo")
ejercicio20("programacion")
ejercicio21("hola mundo")
ejercicio22("banana", "a")
ejercicio23("banana")
ejercicio24("Hola mundo esta es una prueba")
ejercicio25("Hola mundo esta es una prueba")
ejercicio26("Hola hola mundo, hola a todos", "hola")
ejercicio27("   Hola mundo   ")
ejercicio28("Hola mundo")
ejercicio29("abc xyz ABC XYZ")
ejercicio30("Hola mundo esta es una prueba")
