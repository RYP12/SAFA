def realizar_encuesta(preguntas, num_personas):
    respuestas = {pregunta: [] for pregunta in preguntas}

    for i in range(num_personas):
        print(f"-------------------------ENTREVISTADO {i + 1}-------------------------")
        for pregunta in preguntas:
            respuesta = input(f"{pregunta} ")
            respuestas[pregunta].append(respuesta)

    print("-----------------------RESUMEN ENCUESTA----------------------")
    for i, pregunta in enumerate(preguntas):
        print("---------------------------------------------------------------------------")
        print(f"pregunta {i + 1} → {pregunta}")
        print(f"respuestas → {respuestas[pregunta]}")
    print("---------------------------------------------------------------------------")


# Ejemplo de uso
preguntas = ["¿Cuál es tu color favorito?", "¿Cuántos años tienes?"]
num_personas = 3
realizar_encuesta(preguntas, num_personas)
