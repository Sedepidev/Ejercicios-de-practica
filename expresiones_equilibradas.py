'''
La idea es crear un programa que compruebe si los parentesis, llaves y corchetes, de una
expresion, estan equilibrados.
Si los delimitadores se abren y cierran en orden y de formaa correcta.
Los tres tienen la misma prioridad.
'''

def esta_equilibrada(expresion: str) -> bool:
    pila = []

    aperturas = {'(', '[', '{'}
    cierres = {')', ']', '}'}
    pareja = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in aperturas:
            pila.append(caracter)
        elif caracter in cierres:
            if not pila:
                return False
            if pila[-1] != pareja[caracter]:
                return False
            pila.pop()
    
    return len(pila) == 0

def analizar_expresion(expresion: str) -> None:
    resultado = esta_equilibrada(expresion)
    estado = "Equilibrada" if resultado else "No equilibrada"
    print('Expresion: ', expresion)
    print('Resultado: ', estado)

entrada = input('Introduce una expresion:  ')
analizar_expresion(entrada)