'''
La idea es crear un programa que verifique si una cadena es un palindromo.
Retorna True o False, segun sea o no un palindromo.
No se tienen en cuanta espacios, signos de puntuacion y tildes.
Ejemplo: Ana lleva al oso la avellana.
'''


import unicodedata
import re

def es_palindromo(cadena: str) -> bool:
    normalizada = unicodedata.normalize('NFD', cadena.lower())
    solo_letras = re.sub(r'[^a-z0-9]', '', normalizada)
    return solo_letras == solo_letras[::-1]

ejemplos = [
    "Ana lleva al oso la avellana",
    "A man a plan a canal Panama",
    "Yo soy",
    "Hola mundo",
    "Reconocer",
    "Anita lava la tina"
]

for frase in ejemplos:
    resultado = es_palindromo(frase)
    print(f"{resultado!s:<5}  →  {frase!r}")