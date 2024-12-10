tablero = [[0,1,2],[3,4,5],[6,7,8]]  # Creamos una lista bidimensional con las posiciones del tablero, inicializadas de 0 a 8

jugadorX = input("Ingrese tu nombre jugadorX: ")  # Creamos una variable para almacenar el nombre del jugador X
jugadorO = input("Ingrese tu nombre jugadorO: ")  # Creamos una variable para almacenar el nombre del jugador O

# Función que pinta el tablero en la consola
def pinta_tablero():
    for fila in tablero:  # Recorre cada fila del tablero
        print(fila)  # Imprime la fila actual

# Función que verifica si el jugador ha ganado
def ganador(jugador):
    # Comprobación de filas: Si todas las posiciones en una fila son iguales al símbolo del jugador
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == jugador:  # Verifica las horizontales
            return True

    # Comprobación de columnas: Verifica si todas las posiciones de una columna son iguales al símbolo del jugador
    for i in range(3):  # Repite 3 veces (una por columna)
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:  # Verifica las verticales
            return True

    # Comprobación de diagonales:
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:  # Diagonal de izquierda a derecha
        return True

    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:  # Diagonal de derecha a izquierda
        return True

    return False  # Si no se encontró un ganador, retorna False

# Función para que el jugador coloque su pieza
def colocar_pieza(jugador):
    posicion = int(input("Ingrese la posicion donde quieres colocar tu pieza: "))  # El jugador ingresa la posición donde colocar su pieza
    posicion_valida = 0  # Variable para indicar si la posición es válida

    # Recorremos las filas y columnas del tablero
    for i in range(len(tablero)):  # Recorre las filas del tablero
        for j in range(len(tablero[i])):  # Recorre las columnas de cada fila
            if tablero[i][j] == posicion:  # Si el valor de la celda coincide con la posición ingresada por el jugador
                tablero[i][j] = jugador  # Coloca la pieza (X u O) en el tablero
                posicion_valida = 1  # Marca la posición como válida

    # Si la posición ingresada no era válida (la casilla ya estaba ocupada)
    if posicion_valida == 0:
        print("Tu pieza no puede colocar")  # Imprime un mensaje de error
        colocar_pieza(jugador)  # Llama de nuevo a la función para que el jugador vuelva a intentar

# Inicia el juego
pinta_tablero()  # Pinta el tablero inicial

turnos = 1  # Variable que indica el turno actual

# Bucle para permitir hasta 9 turnos (ya que el tablero tiene 9 posiciones)
for i in range(9):
    if turnos % 2 == 0:  # Si el número de turno es par, es el turno del jugador X
        print("Es el turno de ", jugadorX)
        colocar_pieza("X")  # El jugador X coloca su pieza
        pinta_tablero()  # Pinta el tablero actualizado
    else:  # Si el número de turno es impar, es el turno del jugador O
        print("Es el turno de", jugadorO)
        colocar_pieza("O")  # El jugador O coloca su pieza
        pinta_tablero()  # Pinta el tablero actualizado

    # Verifica si el jugador X ha ganado
    if ganador("X"):
        print(jugadorX, "ha hecho 3 en raya")  # Informa que el jugador X ha ganado
        break  # Termina el juego si hay un ganador

    # Verifica si el jugador O ha ganado
    if ganador("O"):
        print(jugadorO, "ha hecho 3 en raya")  # Informa que el jugador O ha ganado
        break  # Termina el juego si hay un ganador

    turnos += 1  # Incrementa el número de turnos

# Si después de los 9 turnos no hay un ganador, se declara empate
if not ganador("X") and not ganador("O"):  # Si ninguno ha ganado
    print("El juego terminó en empate.")  # Informa que el juego ha terminado en empate
# Función para mostrar el tablero
def imprimir_tablero():
    for fila in tablero:
        print(fila)


# Función para verificar si hay un ganador
def hay_ganador(jugador):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == jugador:
            return True

    # Verificar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False


# Función para colocar una pieza en el tablero
def colocar_pieza(jugador):
    while True:
        try:
            posicion = int(input(f"Ingrese la posición donde {jugador} quiere colocar su pieza (0-8): "))
            if posicion < 0 or posicion > 8:
                print("Posición inválida. Debe estar entre 0 y 8.")
                continue

            # Buscar la posición en el tablero
            for i in range(3):
                for j in range(3):
                    if tablero[i][j] == posicion:
                        tablero[i][j] = jugador
                        return
            print("Esa posición ya está ocupada. Elige otra.")
        except ValueError:
            print("Debes ingresar un número válido.")


# Empezamos el juego
turnos = 1
imprimir_tablero()

for i in range(9):
    if turnos % 2 != 0:
        print(f"Es el turno de {jugadorX} (X)")
        colocar_pieza("X")
    else:
        print(f"Es el turno de {jugadorO} (O)")
        colocar_pieza("O")

    imprimir_tablero()

    # Verificar si hay un ganador
    if hay_ganador("X"):
        print(f"{jugadorX} ha hecho 3 en raya. ¡Ganaste!")
        break
    if hay_ganador("O"):
        print(f"{jugadorO} ha hecho 3 en raya. ¡Ganaste!")
        break

    turnos += 1

if not hay_ganador("X") and not hay_ganador("O"):
    print("El juego terminó en empate.")