numero = int(input("Ingrese un numero: "))

veces = int(input("Ingrese las veces: "))

lista = []

for i in range(veces):

    i += 1
    x = numero * i
    lista.append(x)

print(lista)