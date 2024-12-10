def encontrar_divisibles(numero):
    divisibles = [i for i in range(1, 11) if numero % i == 0]
    return divisibles

def mostrar_divisibles(numero):
    divisibles = encontrar_divisibles(numero)
    print(f"Es divisible por {divisibles}")

# Ejemplo de uso
entrada = int(input("Introduce un número: "))
mostrar_divisibles(entrada)
