'''
La idea es crear un programa que pase la primera letra de cada palabra a
mayuscula.
Sin usar operaciones del lenguaje que lo hagan de forma automatica.
'''

def primera_mayuscula(texto: str) -> str:
    if not isinstance(texto, str):
        raise TypeError('El argumento debe de ser un string')
    DIFERENCIA = ord('a') - ord('A')

    def mayuscula(caracter: str) -> str:
        if 'a' <= caracter <= 'z':
            return chr(ord(caracter) - DIFERENCIA)
        return caracter

    palabras = texto.split(' ')
    resultado = []

    for palabra in palabras:
        if palabra:
            resultado.append(mayuscula(palabra[0]) + palabra[1:])
        else:
            resultado.append(palabra)

    return ' '.join(resultado)

print(primera_mayuscula("hola mundo"))
print(primera_mayuscula("hola mundo como estas"))
print(primera_mayuscula("eL gAtO nEgRo"))
