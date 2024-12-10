# Se desea realizar un programa que recibe como parámetro un texto.
# El programa debe devolver el número de letras que sean mayúsculas y consonantes en el texto.
# A continuación se muestra un posible ejemplo de ejecución del programa.
# Cuando el programa recibe los siguientes parámetros:

texto = "Finalmente tras el día de ayer el Real Madrid y el Barcelona siguen adelante en la Copa del Rey"


def contar_mayusculas_consonantes(texto):
    # Definir las consonantes mayúsculas
    consonantes_mayusculas = "BCDFGHJKLMNPQRSTVWXYZ"

    # Contar las consonantes mayúsculas
    contador = 0
    for letra in texto:
        if letra in consonantes_mayusculas:
            contador += 1

    return contador


# Ejemplo de uso

resultado = contar_mayusculas_consonantes(texto)
print(f"El número de letras mayúsculas y consonantes en el texto es: {resultado}")
