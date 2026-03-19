'''
Crea dos funciones, una que calcule el mcd y otra
que calcule el mcm de dos numeros enteros.
- No se pueden utilizar operaciones del lenguaje que
lo resuelvan directamente.
'''


def mcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos argumentos deben ser enteros')
    if a <= 0 or b <= 0:
        raise ValueError('Ambos argumentos deben ser mayores que cero')
    
    while b != 0:
        a, b = b, a % b

    return a

def mcm(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos argumentos deben ser enteros")
    if a <= 0 or b <= 0:
        raise ValueError("Ambos argumentos deben ser mayores que cero")

    return (a * b) // mcd(a, b)

print(mcd(12, 8))
print(mcd(100, 75))
print(mcd(17, 13))
print(mcd(9, 9))

print()

print(mcm(4, 6))
print(mcm(3, 5))
print(mcm(12, 8))
print(mcm(9, 9))