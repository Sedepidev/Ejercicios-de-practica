'''
Crear un programa que invierta el orden de una cadena de texto, sin usar funciones propias del lenguaje
que lo hagan de forma automatica.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def invertir_cadena(texto):
    
    resultado = ""  # aquí iremos acumulando los caracteres al revés

    # len(texto) nos da el total de caracteres, por ejemplo 10
    # El último índice válido es len(texto) - 1, es decir 9
    # Empezamos desde ahí y vamos bajando hasta 0 (inclusive)
    indice = len(texto) - 1

    while indice >= 0:
        resultado = resultado + texto[indice]  # añadimos letra por letra
        indice = indice - 1                    # retrocedemos una posición

    return resultado


def main():
    print("=== Inversor de cadenas ===")
    texto = input("Ingresa un texto: ")

    if texto == "":
        print("No ingresaste ningún texto.")
        return

    invertido = invertir_cadena(texto)

    print(f"Original: {texto}")
    print(f"Invertido: {invertido}")


if __name__ == "__main__":
    main()