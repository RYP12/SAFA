#Se desea realizar un programa que recibe como parámetro una lista de números.
#El programa debe devolver una lista, con los números que no tengan decimales y que se puedan
#dividir entre 2 y 3 . A continuación se muestra un ejemplo de ejecución del programa.

lista_numeros = [4.5 , 6 , 10.3 , 12.4 , 15.0 , 18 , 24 ]

for entero in lista_numeros:
    if entero >= 0 and entero % 2 == 0 and entero % 3 == 0:

        print(entero)
