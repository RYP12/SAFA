import requests
from bs4 import BeautifulSoup


#HACER PETICIÓN A LA PÁGINA WEB PARA OBTENER CODIGO FUENTE
# -> 200 OK
# requests -> get("url de la página web")
url = "https://www.padelchiquito.com/mejores-palas-2024/"
contenido = requests.get(url).content


#Tranformar el contenido de la página web -> soup
# bs4 -> BeautifulSoup (contenido-> soup)
soup = BeautifulSoup(contenido, "html.parser")



#Buscamos los contenedores principales de nuestros elementos
contenedores = soup.find_all('a', {'class': 'flex flex-col md:max-w-[30rem] items-start gap-4 p-4 text-center transition-transform hover:scale-105'})


#DICCIONARIO
pala = {
    "nombre": None,
    "foto": None,
    "marca":None,
    "forma": None,
    "tacto": None,
    "temporada": None,
    "precio": None
}




lista = []

for contenedor in contenedores:

    if contenedor.find('h3') is not None:

        #COPIO EL DICCIONARIO PLANTILLA
        nueva_pala = pala.copy()


        #nombre
        nombre_pala = contenedor.find('h3').text
        nueva_pala["nombre"] = nombre_pala
        #print(nombre_pala)

        #Imagen
        imagen = contenedor.find('img')['src']
        nueva_pala["foto"] = imagen
        #print(imagen)

        #Propiedades
        info_propiedades = contenedor.find('div',{'class': 'flex flex-wrap items-center text-xs'})
        marca = info_propiedades.find_all('span')[0].text
        forma = info_propiedades.find_all('span')[1].text
        tacto = info_propiedades.find_all('span')[2].text
        anyo = info_propiedades.find_all('span')[3].text

        nueva_pala["marca"] = marca
        nueva_pala["forma"] = forma
        nueva_pala["tacto"] = tacto
        nueva_pala["temporada"] = anyo

        #print(marca, forma, tacto,anyo)


        #Precio
        precio = float(contenedor.find('span', {'class': 'flex flex-col px-2 py-1 text-sm font-semibold rounded-full bg-acid-pops'}).text.replace('\n','').replace('Desde','').replace('€',''))
        nueva_pala["precio"] = precio
        #print(precio)



        # #ENLACE
        # enlace = contenedor['href']
        # contenido = requests.get(enlace)
        # soup = BeautifulSoup(contenido,'html.parser')



        print(nueva_pala)
        lista.append(nueva_pala)


