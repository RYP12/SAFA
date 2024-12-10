def calcular_media_y_clasificar(notas):
    # Calcular la media de las notas
    media = sum(notas) / len(notas)

    # Clasificar según la media obtenida
    if media < 5:
        return "Suspenso"
    elif 5 <= media < 7:
        return "Aprobado"
    elif 7 <= media < 9:
        return "Notable"
    else:
        return "Sobresaliente"


# Ejemplo de uso
notas = [5.6, 7, 6.2, 8]
media_calculada = sum(notas) / len(notas)
resultado = calcular_media_y_clasificar(notas)
print(f"La media calculada sería : {media_calculada}")
print(f"El método devolvería: {resultado}")
