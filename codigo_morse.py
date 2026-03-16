'''
La idea es crear un programa que traduzca el texto a codigo morse y al reves.
El alfabeto morse soportado sera el de https://es.wikipedia.org/wiki/Código_morse
'''


MORSE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--'
}

MORSE_INVERSO = {v: k for k, v in MORSE.items()}


def texto_a_morse(texto):
    palabras = []
    for palabra in texto.upper().split(' '):
        letras = [MORSE.get(c, '?') for c in palabra]
        palabras.append(' '.join(letras))
    return '   '.join(palabras)


def morse_a_texto(morse):
    resultado = []
    for palabra in morse.split('   '):
        for codigo in palabra.split(' '):
            if codigo in MORSE_INVERSO:
                resultado.append(MORSE_INVERSO[codigo])
            elif codigo == '':
                continue
            else:
                resultado.append('?')
        resultado.append(' ')
    return ''.join(resultado).strip()


if __name__ == '__main__':
    print("=== Conversor Morse ===")
    print("1. Texto → Morse")
    print("2. Morse → Texto")
    opcion = input("Elige opción (1/2): ").strip()

    if opcion == '1':
        texto = input("Texto: ")
        print("Morse:", texto_a_morse(texto))
    elif opcion == '2':
        print("Morse (1 espacio entre letras, 3 espacios entre palabras):")
        morse = input("> ")
        print("Texto:", morse_a_texto(morse))
    else:
        print("Opción no válida.")