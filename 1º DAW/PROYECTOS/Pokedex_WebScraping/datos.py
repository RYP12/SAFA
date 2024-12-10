from PySide6.scripts.pyside_tool import designer

import scraping as pokedex
import csv
import pandas as pd
import mysql.connector as mysql

def convertir_csv ():
    lista_datos = pokedex.lista_pokemons
    with open("pokedex.csv", "w", newline="", encoding='utf-8') as archivo_pokedex:
        escritor = csv.writer(archivo_pokedex)

        escritor.writerow(lista_datos[0].keys())

        for pokemos in lista_datos:
            escritor.writerow(pokemos.values())

def convertir_a_excel ():
    archivo_csv = pd.read_csv("pokedex.csv")
    archivo_exel= archivo_csv.to_excel("pokedex.xlsx", index=False)



def mostrar_excel():
    archivo_excel = pd.read_excel("pokedex.xlsx",engine='openpyxl')
    print(archivo_excel)

def conectar_bbdd():

    #Parámetros de conexion
    parametros_conexion = {
        'user': 'daw',
        'password': '1234',
        'host': 'localhost',
        'database': 'pokedex',
        'port': 3306,
        'charset': 'utf8mb4',
        'collation': 'utf8mb4_general_ci',
        'use_unicode': True,
        'autocommit': True
    }

    #Devuelve la conexion establecida con la bbdd
    return mysql.connect(**parametros_conexion)

def volcado_datos():

    #Obtenemos los coódigos de nuestros métodos web scraping
    lista_pokemons = pokedex.scraping_pokemons()

    #Abrimos conexion con la base de datos
    conexion = conectar_bbdd()

    #Abrimos cursor
    cursor = conexion.cursor()

    #Sentencia INSERT
    scrip_insercion = "INSERT INTO pokemon (codigo, img, nombre, mega, tipo_1, tipo_2, total_pc) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    #Cada pokemon se convierte en una script de insercion

    for pokemon in lista_pokemons:
        cursor.execute(scrip_insercion,(pokemon['codigo'],pokemon['img'],pokemon['nombre'],pokemon['mega'],pokemon['tipo_1'],pokemon['tipo_2'],pokemon['total_pc']))

        # Commit para guardar los cambios
    conexion.commit()
    cursor.close()
        #Cerramos conexion con la base de datos
    conexion.close()

def consultar_datos():

    #Abrir conexion
    conexion = conectar_bbdd()

    #abrir cursor
    cursor = conexion.cursor(dictionary=True)

    #Lista de elementos
    lista_pokemons = []

    #Script de consulta (SELECT)
    script_consulta = "SELECT * FROM pokemon"

    #Ejecutar la consulta
    cursor.execute(script_consulta)

    #Nos traemos los datos de la consulta anterior
    lista_pokemons = cursor.fetchall()

    #cerramos conexion
    conexion.close()

    return lista_pokemons

def eliminar (id):

    #Abrir conexion
    conexion = conectar_bbdd()

    #Abrir Cursor
    cursor = conexion.cursor()

    #Sript Eliminar (DELETE FROM tabla where id = num)
    script_eleminar = "delete from pokemon where id =" + str(id)

    #Ejecutar Script
    cursor.execute(script_eleminar)

    #Cerrar conexion
    conexion.close()


volcado_datos()











