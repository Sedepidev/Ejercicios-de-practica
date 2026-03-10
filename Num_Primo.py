'''
Programa para verificar si es un numero primo o no primo.
Luego imprime todos los numeros primos entre 1 y 100
'''

def es_primo(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


print(es_primo(int(input("Escribe el numero que quieras comprobar: "))))