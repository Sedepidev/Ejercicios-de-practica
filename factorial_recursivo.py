'''
Escribe una funcion que calcule y retorne el factorial de un numero
dado de forma recursiva
'''


def factorial(n):
    if n < 0:
        raise ValueError('El factorial no esta definido para numeros negativos')
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(10))
print(factorial(int(input('Escribe el numero que quieras factorizar: '))))
