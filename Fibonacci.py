'''
Programa para imprimir los primeros 50 digitos de la sucesion de Fibonacci.
La serie de Fibonacci se compone de una sucesion de numeros en la cual el numero
siguiente siempre es la suma de los dos numeros anteriores
0, 1, 1, 2, 3, 5, 8, 13...
'''


def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a)
        a, b = b, a + b

fibonacci(50)