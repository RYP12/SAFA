import requests
from bs4 import BeautifulSoup

# Página Web de Pokémon
def obtener_contenido():
    url = "https://pokemondb.net/pokedex/all"
    #Extraigo el contenido de la página
    contenido = requests.get(url).content
    return contenido

# Transformar el contenido de la página web -> sopa
def convertir_sopa():
    contenido = obtener_contenido()
    #Convierto el contenido de la página en un formato más visual
    soup = BeautifulSoup(contenido, "html.parser")
    #Al investigar la página, visualizo todos los datos en una tabla y la selecciono
    pokedex = soup.find("table", class_="data-table sticky-header block-wide")
    return pokedex

#Variable que almacenamos el html de la tabla donde se encuentran los datos
full_pokedex = convertir_sopa()

# Lista donde se incluira cada pokemon con sus datos
lista_pokemons = []
# Función que extrae los datos en conxreto de los pokemons y los almacena
def scraping_pokemons():
    # Bucle que recorre toda la tabla y recopilalos datos de cada pokemon
    for lista in full_pokedex.find("tbody").find_all("tr"):
        #Diccioario con los elementos principales de cada pokemon
        pokemon = {
            "img" : None,
            "codigo": None,
            "nombre": None,
            "mega": None,
            "tipo_1": None,
            "tipo_2": None,
            "total_pc": None,

        }
        # IMAGEN
        img_pokemon = lista.find('img', class_="img-fixed icon-pkmn")["src"]
        # Se clasifica como un atributo del diccionario
        pokemon["img"] = img_pokemon
        # ID
        id_pokemon = lista.find('td', class_="cell-num cell-fixed").find('span').text
        # Se clasifica como un atributo del diccionario
        pokemon["codigo"] = id_pokemon
        # NOMBRE
        nombre_pokemon = lista.find('a', class_="ent-name").text
        # Se clasifica como un atributo del diccionario
        pokemon["nombre"] = nombre_pokemon
        #MEGA EVOLUCIÓN
        mega_pokemon = lista.find('small', class_="text-muted")
        # En caso de que presente mega evolución se añade su nombre en el atributo correspondiente
        if mega_pokemon:
            # Se clasifica como un atributo del diccionario
            pokemon["mega"] = mega_pokemon.text
        # TIPOS
        tipos_pokemon = lista.find_all('a', class_="type-icon")
        # Al poder tener más de un tipo y como máximo dos, con el if se coloca en su respectivo atributo
        if len(tipos_pokemon) > 0:
            # Se clasifica como un atributo del diccionario
            pokemon["tipo_1"] = tipos_pokemon[0].text
            if len(tipos_pokemon) > 1:
                # Se clasifica como un atributo del diccionario
                pokemon["tipo_2"] = tipos_pokemon[1].text
        # PUNTOS DE COMBATE
        total_pc_pokemon = lista.find('td', class_="cell-num cell-total").text
        pokemon["total_pc"] = total_pc_pokemon
        # Se añade cada diccionario de cada pokemon en la lista
        lista_pokemons.append(pokemon)
    # Devuelve la funcion la lista
    return lista_pokemons
# Bucle para visualizar la lista donde estan todos los pokemons




