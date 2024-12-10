def normalizar_texto(texto):
    # Convertir el texto a minúsculas y reemplazar las vocales con tildes por sus equivalentes sin tilde
    texto = texto.lower()
    texto = texto.replace('á', 'a')
    texto = texto.replace('é', 'e')
    texto = texto.replace('í', 'i')
    texto = texto.replace('ó', 'o')
    texto = texto.replace('ú', 'u')
    return texto


def contar_palabras(lista_palabras, texto):
    # Normalizar el texto
    texto_normalizado = normalizar_texto(texto)

    # Crear un diccionario para contar las apariciones
    recuento = {palabra: 0 for palabra in lista_palabras}

    # Contar las palabras en el texto
    for palabra in lista_palabras:
        palabra_normalizada = normalizar_texto(palabra)
        recuento[palabra] = texto_normalizado.split().count(palabra_normalizada)

    # Imprimir los resultados
    print("— RECUENTO DE PALABRAS —")
    for palabra, cuenta in recuento.items():
        print(f"{palabra} : {cuenta}")


# Ejemplo de uso
texto = """Ey, Tití me preguntó
Si tengo muchas novia'
Muchas novia'
Hoy tengo a una, mañana otra
Ey, pero no hay boda
Tití me preguntó
Si tengo muchas novia'
Je, muchas novia'
Hoy tengo a una, mañana otra"""

lista_palabras = ["TITI", "Novia'", "Casa", "bunny"]
contar_palabras(lista_palabras, texto)
