#Se desea realizar un programa de valoración de futbolistas , para ello el programa recibe:
#   ● La lista con los nombres de los futbolistas que se van a valorar.
#   ● El número de personas a las que se va a preguntar por la nota que le ponen a los futbolistas.
#El programa debe decir por consola a cada futbolista y las personas dirán la valoración que le ponen .
#Al final deberá mostrar por consola la media de puntuación obtenida por cada futbolista. A
#continuación se muestra un ejemplo



def valorar_futbolistas(futbolistas, num_personas):
    valoraciones = {futbolista: [] for futbolista in futbolistas}

    for futbolista in futbolistas:
        print(f"-------------------------VALORACIÓN {futbolista.upper()}-------------------------")
        for i in range(1, num_personas + 1):
            valor = int(input(f"Persona {i} → "))
            valoraciones[futbolista].append(valor)

    print("-----------------------RESUMEN VALORACIONES ----------------------")
    for futbolista, notas in valoraciones.items():
        media = sum(notas) / len(notas)
        print(f"{futbolista} (Media Obtenida) → {media}")
    print("---------------------------------------------------------------------------")


# Ejemplo de uso
futbolistas = ["Haaland", "Mbappe", "Vinicius Jr"]
num_personas = 3
valorar_futbolistas(futbolistas, num_personas)

