'''
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre 
el recuento final de todas ellas.
Los signos de puntuación no forman parte de la palabra.
Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''

def es_puntuacion(caracter):
    """
    Devuelve True si el carácter es un signo de puntuación.
    Definimos manualmente qué consideramos puntuación.

    Ejemplo:
        es_puntuacion(',') → True
        es_puntuacion('a') → False
    """
    signos = '.,;:!¡?¿"\'-()[]{}...'
    return caracter in signos  # comprueba si el carácter está en la cadena de signos


def limpiar_palabra(palabra):
    """
    Recorre la palabra carácter a carácter y elimina
    cualquier signo de puntuación que encuentre.

    Ejemplo:
        limpiar_palabra("hola,") → "hola"
        limpiar_palabra("'mundo'") → "mundo"
    """
    resultado = ''
    for char in palabra:
        if not es_puntuacion(char):
            resultado += char  # solo añadimos si NO es puntuación
    return resultado


def a_minusculas(cadena):
    """
    Convierte una cadena a minúsculas usando códigos ASCII.

    ¿Qué es ord() y chr()?
        ord('A') → 65   (devuelve el número ASCII del carácter)
        chr(65)  → 'A'  (devuelve el carácter de ese número ASCII)

    En la tabla ASCII las mayúsculas van del 65 (A) al 90 (Z)
    y sus minúsculas equivalentes van del 97 (a) al 122 (z).
    La diferencia entre mayúscula y minúscula es siempre 32.

    Entonces: ord('A') + 32 = 97 = ord('a')  ✓

    Ejemplo:
        a_minusculas("Hola") → "hola"
        a_minusculas("MUNDO") → "mundo"

    Nota: solo convierte letras A-Z sin tilde. Las letras con
    tilde (Á, É...) no están en ese rango ASCII y se dejan igual.
    """
    resultado = ''
    for char in cadena:
        codigo = ord(char)                  # obtenemos el número ASCII del carácter
        if 65 <= codigo <= 90:              # ¿está entre 'A' y 'Z'?
            resultado += chr(codigo + 32)   # lo convertimos a minúscula sumando 32
        else:
            resultado += char              # ya es minúscula u otro carácter, lo dejamos igual
    return resultado


def contar_palabras(texto):
    """
    Recorre el texto carácter a carácter, construye palabras
    y las cuenta en un diccionario.

    ¿Cómo funciona el diccionario de conteo?
        conteo = {"hola": 2, "mundo": 1}
        - la clave   es la palabra
        - el valor   es cuántas veces apareció

    Ejemplo:
        "Hola hola mundo" → {"hola": 2, "mundo": 1}
    """
    palabra_actual = ''  # vamos acumulando letras aqui
    conteo = {}          # diccionario vacio donde guardaremos el recuento

    for char in texto:
        if char.isalnum() or char == '\'':
            # isalnum() devuelve True si el carácter es letra o número
            # también permitimos el apóstrofe ' para palabras como "l'estrella o en ingles, don't"
            palabra_actual += char  # seguimos construyendo la palabra

        else:
            # Encontramos un separador (espacio, coma, punto...)
            # → la palabra actual ha terminado, la procesamos
            if palabra_actual:                                          # si no está vacía
                palabra_limpia = limpiar_palabra(palabra_actual)   # quitamos puntuación
                palabra_normalizada = a_minusculas(palabra_limpia)      # pasamos a minúsculas

                if palabra_normalizada:  # comprobamos que no quedó vacía tras limpiar
                    if palabra_normalizada in conteo:
                        conteo[palabra_normalizada] += 1  # ya existía → sumamos 1
                    else:
                        conteo[palabra_normalizada] = 1   # nueva palabra → empezamos en 1

                palabra_actual = ''  # reiniciamos para la siguiente palabra

    # Si el texto no termina en espacio o puntuación, el bucle
    # termina sin haber procesado la última palabra acumulada.
    # Este bloque la procesa exactamente igual que dentro del bucle.
    if palabra_actual:
        palabra_limpia = limpiar_palabra(palabra_actual)
        palabra_normalizada = a_minusculas(palabra_limpia)

        if palabra_normalizada:
            if palabra_normalizada in conteo:
                conteo[palabra_normalizada] += 1
            else:
                conteo[palabra_normalizada] = 1

    return conteo


def mostrar_conteo(conteo):
    """
    Imprime cada palabra junto a su número de apariciones.

    conteo.items() devuelve pares (clave, valor), es decir
    (palabra, cantidad), lo que nos permite recorrerlos juntos.
    """
    print("\nRecuento de palabras:")
    print("-" * 30)
    for palabra, cantidad in conteo.items():
        print(f"{palabra}: {cantidad}")


# ─────────────────────────────────────────────────────────────
# TEXTO DE PRUEBA Y EJECUCIÓN
# ─────────────────────────────────────────────────────────────
texto_ejemplo = """El veloz murcielago hindu comia feliz cardillo y kiwi. 
La cigena tocaba el saxofon mientras el murcielago volaba. 
El cardillo era feliz con el veloz murcielago."""

resultado = contar_palabras(texto_ejemplo)
mostrar_conteo(resultado)