'''
La idea es crear un programa que pase un numero decimal
a binario, sin usar herramientas integradas del propio lenguaje
'''


def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    
    return binario


numero = int(input("Ingresa un número decimal: "))
resultado = decimal_a_binario(numero)
print(f"El número binario es: {resultado}")
