
lista_coches = [
    {
        "modelo": "Gallardo",
        "marca": "Lamborghini",
        "tipo": "Deportivo",
        "puertas": 3
    },
    {
        "modelo": "Murciélago GT",
        "marca": "Lamborghini",
        "tipo": "Carrera",
        "puertas": 2
    },
    {
        "modelo": "Twingo",
        "marca": "Renault",
        "tipo": "Normal",
        "puertas": 5
    }
]




def coches_con_mas_de_dos_puertas(lista_coches):
    coches_filtrados = [coche['modelo'] for coche in lista_coches if coche['puertas'] > 2]
    coches_ordenados = sorted(coches_filtrados, key=lambda coche: next(c['puertas'] for c in lista_coches if c['modelo'] == coche))
    return coches_ordenados



resultado_a = coches_con_mas_de_dos_puertas(lista_coches)
print(resultado_a)


def coches_por_marca(lista_coches, marca):
    coches_filtrados = [coche for coche in lista_coches if coche['marca'] == marca]
    return coches_filtrados

# Ejemplo de uso
resultado_b = coches_por_marca(lista_coches, "Lamborghini")
print(resultado_b)
# [{'modelo': 'Gallardo', 'marca': 'Lamborghini', 'tipo': 'Deportivo', 'puertas': 3}, {'modelo': 'Murciélago GT', 'marca': 'Lamborghini', 'tipo': 'Carrera', 'puertas': 2}]


def construir_lista_diccionarios(modelos, marcas, tipos, puertas):
    lista_diccionarios = []
    for modelo, marca, tipo, puerta in zip(modelos, marcas, tipos, puertas):
        lista_diccionarios.append({
            "modelo": modelo,
            "marca": marca,
            "tipo": tipo,
            "puertas": puerta
        })
    return lista_diccionarios

# Ejemplo de uso
modelos = ["Gallardo", "Murciélago GT", "Twingo"]
marcas = ["Lamborghini", "Lamborghini", "Renault"]
tipos = ["Deportivo", "Carrera", "Normal"]
puertas = [3, 2, 5]

resultado_c = construir_lista_diccionarios(modelos, marcas, tipos, puertas)
print(resultado_c)
# [{'modelo': 'Gallardo', 'marca': 'Lamborghini', 'tipo': 'Deportivo', 'puertas': 3}, {'modelo': 'Murciélago GT', 'marca': 'Lamborghini', 'tipo': 'Carrera', 'puertas': 2}, {'modelo': 'Twingo', 'marca': 'Renault', 'tipo': 'Normal', 'puertas': 5}]
