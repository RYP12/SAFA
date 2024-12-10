lista_pokemon = [
    {
        "nombre": "Treecko",
        "pokédex": 252,
        "tipo": ["PLANTA"],
        "evo": 1
    },
    {
        "nombre": "Roselia",
        "pokédex": 407,
        "tipo": ["PLANTA", "VENENO"],
        "evo": 2
    },
    {
        "nombre": "Milotic",
        "pokédex": 350,
        "tipo": ["AGUA"],
        "evo": 2
    },
    {
        "nombre": "Altaria",
        "pokédex": 334,
        "tipo": ["VOLADOR", "DRAGÓN"],
        "evo": 2
    }
]







def ordenar_por_pokedex(lista_pokemon):
    return sorted(lista_pokemon, key=lambda x: x['pokédex'], reverse=True)

# Ejemplo de uso
lista_pokemon = [
    {"nombre": "Treecko", "pokédex": 252, "tipo": ["PLANTA"], "evo": 1},
    {"nombre": "Roselia", "pokédex": 407, "tipo": ["PLANTA", "VENENO"], "evo": 2},
    {"nombre": "Milotic", "pokédex": 350, "tipo": ["AGUA"], "evo": 2},
    {"nombre": "Altaria", "pokédex": 334, "tipo": ["VOLADOR", "DRAGÓN"], "evo": 2}
]

resultado_a = ordenar_por_pokedex(lista_pokemon)
print(resultado_a)

def filtrar_por_tipo(lista_pokemon, tipo):
    tipo_mayusculas = tipo.upper()
    return [pokemon for pokemon in lista_pokemon if tipo_mayusculas in pokemon['tipo']]

# Ejemplo de uso
resultado_b = filtrar_por_tipo(lista_pokemon, "PLANTA")
print(resultado_b)

def construir_lista_pokemon(nombres, numeros, tipos, evo):
    return [{"nombre": nombre, "pokédex": numero, "tipo": tipo, "evo": evolucion}
            for nombre, numero, tipo, evolucion in zip(nombres, numeros, tipos, evo)]

# Ejemplo de uso
nombres = ["Treecko", "Roselia", "Milotic", "Altaria"]
numeros = [252, 407, 350, 334]
tipos = [["PLANTA"], ["PLANTA", "VENENO"], ["AGUA"], ["VOLADOR", "DRAGÓN"]]
evo = [1, 2, 2, 2]

resultado_c = construir_lista_pokemon(nombres, numeros, tipos, evo)
print(resultado_c)
