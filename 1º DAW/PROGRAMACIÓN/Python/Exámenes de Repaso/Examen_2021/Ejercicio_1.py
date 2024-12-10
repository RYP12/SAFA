def contar_signos_puntuacion(texto):
    # Definir los signos de puntuación a contar
    signos_puntuacion = {
        'comas': [','],
        'puntos': ['.'],
        'interrogaciones': ['?', '¿'],
        'exclamaciones': ['!', '¡'],
        'dos puntos': [':'],
        'punto y coma': [';'],
        'paréntesis': ['(', ')'],
        'corchetes': ['[', ']'],
        'comillas': ['"', "'"],
        'puntos suspensivos': ['...'],
        'diéresis': ['¨'],
        'guion': ['-']
    }

    # Inicializar contadores
    contadores = {key: 0 for key in signos_puntuacion}

    # Recorrer el texto y contar los signos de puntuación
    i = 0
    while i < len(texto):
        char = texto[i]
        for key, signos in signos_puntuacion.items():
            if any(texto[i:i+len(signo)] == signo for signo in signos):
                contadores[key] += 1
                i += len(signos[0]) - 1  # Avanzar el índice para signos de más de un carácter
                break  # Para evitar contar dos veces signos compuestos (e.g., ¿?)
        i += 1

    # Imprimir resultados
    print("Signos de puntuación encontrados:")
    for key, count in contadores.items():
        print(f"Número de {key} : {count}")

# Ejemplo de uso
texto = """En las ciudades de Piltover y Zaun, se palpa el desasosiego en el ambiente: inventores, ladrones,
políticos y señores del crimen buscan liberarse de las ataduras de una sociedad fragmentada.
Mientras la rebelión va cobrando fuerza, dos hermanas roban un artefacto de poder inimaginable.
Los descubrimientos y el peligro son el trasfondo sobre el que nacerán héroes y se romperán vínculos.
¿Servirá este poder para cambiar el mundo o lo llevará a la ruina? Este es el mundo de Arcane."""

contar_signos_puntuacion(texto)
