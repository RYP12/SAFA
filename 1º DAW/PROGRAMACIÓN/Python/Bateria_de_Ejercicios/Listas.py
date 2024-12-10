def ejercicio1():
    # Crea una lista llamada nombres que contenga los nombres de tres compañeros de clase
    nombres = ["Ana", "Juan", "Luis"]

    # Imprime el segundo nombre de la lista
    print("Segundo nombre:", nombres[1])

    # Agrega tu nombre a la lista y muestra la lista actualizada
    nombres.append("TuNombre")
    print("Lista actualizada:", nombres)


def ejercicio2():
    # Dada la siguiente lista de números
    numeros = [1, 2, 3, 4, 5]

    # Cambia el tercer elemento (3) por 10
    numeros[2] = 10

    # Elimina el último número de la lista y muestra la lista resultante
    numeros.pop()
    print("Lista modificada:", numeros)


def ejercicio3():
    # Crea una lista llamada números que contenga los números del 1 al 10
    numeros = list(range(1, 11))

    # Utiliza un bucle for para imprimir cada número de la lista en una línea separada
    for numero in numeros:
        print(numero)


def ejercicio4():
    # Dada la lista de números
    numeros = list(range(1, 11))

    # Crea una nueva lista llamada pares que contenga solo los números pares de la lista original
    pares = [numero for numero in numeros if numero % 2 == 0]

    # Imprime la lista pares
    print("Números pares:", pares)


def ejercicio5():
    # Dada una lista de números
    numeros = [1, 2, 3, 4, 5]

    # Calcula la suma de todos los números en la lista y muestra el resultado
    suma = sum(numeros)
    print("Suma de los números:", suma)


def ejercicio6():
    # Crea una lista que represente una matriz 3x3 (una lista de listas)
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Imprime la matriz en forma de tabla
    for fila in matriz:
        print(" ".join(map(str, fila)))

    # Calcula la suma de todos los elementos en la matriz
    suma = sum(sum(fila) for fila in matriz)
    print("Suma de todos los elementos en la matriz:", suma)


def promedio_lista(numeros):
    # Devuelve el promedio de los números en la lista
    return sum(numeros) / len(numeros)


def ejercicio7():
    # Utiliza la función para calcular el promedio de una lista de números de tu elección
    numeros = [5, 8, 10, 4, 6]
    promedio = promedio_lista(numeros)
    print("Promedio de la lista:", promedio)


def ejercicio8():
    # Crea una lista de calificaciones de alumnos
    calificaciones = [4.5, 6, 7, 3, 9, 5, 4, 8]

    # Determina cuántos alumnos aprobaron (calificación >= 5) y cuántos reprobaron (calificación < 5)
    aprobados = len([nota for nota in calificaciones if nota >= 5])
    reprobados = len([nota for nota in calificaciones if nota < 5])

    # Imprime el número de aprobados y reprobados
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)


def ejercicio9():
    # Crea una lista de nombres desordenados
    nombres = ["Carlos", "Ana", "Luis", "Beatriz", "Juan"]

    # Utiliza el método sort() para ordenar la lista en orden alfabético
    nombres.sort()

    # Imprime la lista ordenada
    print("Lista ordenada:", nombres)


def ejercicio10():
    # Crea una lista de palabras
    palabras = ["gato", "perro", "pájaro", "pez", "hamster"]

    # Permite al usuario ingresar una palabra y determina si esa palabra está en la lista
    palabra_buscada = input("Ingresa una palabra: ")

    # Muestra un mensaje indicando si la palabra fue encontrada o no
    if palabra_buscada in palabras:
        print(f"La palabra '{palabra_buscada}' fue encontrada en la lista.")
    else:
        print(f"La palabra '{palabra_buscada}' no fue encontrada en la lista.")


# Llamada a cada función para ejecutar los ejercicios
ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()
ejercicio6()
ejercicio7()
ejercicio8()
ejercicio9()
ejercicio10()
