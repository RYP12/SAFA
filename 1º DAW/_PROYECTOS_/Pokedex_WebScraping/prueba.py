import mysql.connector

# Parámetros de conexion
parametros_conexion = {
    'user': 'daw',
    'password': '1234',
    'host': 'localhost',
    'database': 'pokedex',
    'port': 3306,
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

conexion = mysql.connector.connect(**parametros_conexion)
print(conexion)

