def mostrar_palabras(lista_palabras, numeros):
    if len(lista_palabras) != len(numeros):
        print("No puedo realizar la operación")
        return

    for palabra, numero in zip(lista_palabras, numeros):
        print((palabra + ' ') * numero)


# Ejemplo de uso
lista_palabras = ["hola", "cómo", "estás"]
numeros = [3, 1, 1]
mostrar_palabras(lista_palabras, numeros)
