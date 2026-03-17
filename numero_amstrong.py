'''
Escribe una funcion que calcule si un numero dado es un numero 
de Armstrong (o narcisista).
'''

def es_armstrong(n):
    if n < 0:
        raise ValueError("El numero debe de ser positivo")
    
    digitos = str(n)
    potencia = len(digitos)
    suma = sum(int(d) ** potencia for d in digitos)

    return suma == n

print(es_armstrong(int(input('Escribe el numero que quieras comprobar: '))))