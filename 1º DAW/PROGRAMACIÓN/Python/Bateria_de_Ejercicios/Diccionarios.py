# Paso 1: Crear un diccionario de juguetes
juguetes = {
    "pelota": 10,
    "muñeca": 15,
    "coche": 20,
    "rompecabezas": 18,
    "peluche": 12,
    "robot": 25,
    "pistola de agua": 8,
    "tren de juguete": 22,
    "oso de peluche": 14,
    "cometa": 10,
    "bloques de construcción": 30,
    "balón de fútbol": 16,
    "patineta": 35,
    "avión de juguete": 24,
    "casa de muñecas": 28
}

# Ejercicio 2: Acceder a un valor en el diccionario
def ejercicio2(juguetes):
    nombre_juguete = input("Ingresa el nombre del juguete: ")
    if nombre_juguete in juguetes:
        print(f"El precio de {nombre_juguete} es {juguetes[nombre_juguete]} euros.")
    else:
        print(f"El juguete {nombre_juguete} no se encuentra en el diccionario.")

# Ejercicio 3: Modificar un valor en el diccionario
def ejercicio3(juguetes):
    nombre_juguete = input("Ingresa el nombre del juguete cuyo precio deseas modificar: ")
    if nombre_juguete in juguetes:
        nuevo_precio = int(input(f"Ingrese el nuevo precio para {nombre_juguete}: "))
        juguetes[nombre_juguete] = nuevo_precio
        print("Diccionario actualizado:", juguetes)
    else:
        print(f"El juguete {nombre_juguete} no se encuentra en el diccionario.")

# Ejercicio 4: Agregar un nuevo juguete al diccionario
def ejercicio4(juguetes):
    nombre_juguete = input("Ingresa el nombre del nuevo juguete: ")
    precio_juguete = int(input(f"Ingrese el precio de {nombre_juguete}: "))
    juguetes[nombre_juguete] = precio_juguete
    print("Diccionario actualizado:", juguetes)

# Ejercicio 5: Recorrer el diccionario de juguetes
def ejercicio5(juguetes):
    for nombre, precio in juguetes.items():
        print(f"{nombre}: {precio} euros")

# Ejercicio 6: Calcular el precio promedio de los juguetes
def ejercicio6(juguetes):
    promedio = sum(juguetes.values()) / len(juguetes)
    print(f"El precio promedio de los juguetes es: {promedio:.2f} euros")

# Ejercicio 7: Eliminar un juguete del diccionario
def ejercicio7(juguetes):
    nombre_juguete = input("Ingresa el nombre del juguete que deseas eliminar: ")
    if nombre_juguete in juguetes:
        del juguetes[nombre_juguete]
        print("Diccionario actualizado:", juguetes)
    else:
        print(f"El juguete {nombre_juguete} no se encuentra en el diccionario.")

# Ejercicio 8: Desafío - Buscar y mostrar juguetes por precio
def ejercicio8(juguetes):
    precio_limite = int(input("Ingresa el precio límite: "))
    juguetes_en_rango = {nombre: precio for nombre, precio in juguetes.items() if precio <= precio_limite}
    print("Juguetes en el rango de precio:")
    for nombre, precio in juguetes_en_rango.items():
        print(f"{nombre}: {precio} euros")

# Ejercicio 9: Desafío - Totalizar el precio de un conjunto de juguetes
def ejercicio9(juguetes):
    lista_compras = input("Ingresa los nombres de los juguetes que deseas comprar, separados por comas: ").split(',')
    total = 0
    for nombre_juguete in lista_compras:
        nombre_juguete = nombre_juguete.strip()
        if nombre_juguete in juguetes:
            total += juguetes[nombre_juguete]
        else:
            print(f"El juguete {nombre_juguete} no se encuentra en el diccionario.")
    print(f"El precio total de los juguetes seleccionados es: {total} euros")

# Ejercicio 10: Desafío - Encontrar el juguete más caro
def ejercicio10(juguetes):
    juguete_mas_caro = max(juguetes, key=juguetes.get)
    print(f"El juguete más caro es {juguete_mas_caro} con un precio de {juguetes[juguete_mas_caro]} euros")

# Llamada a las funciones de ejemplo
ejercicio2(juguetes)
ejercicio3(juguetes)
ejercicio4(juguetes)
ejercicio5(juguetes)
ejercicio6(juguetes)
ejercicio7(juguetes)
ejercicio8(juguetes)
ejercicio9(juguetes)
ejercicio10(juguetes)
