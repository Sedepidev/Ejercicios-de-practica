'''
Crea una funcion que evalue si una atleta ha superado correctamente una
carrera de obstaculos.
- La funcion recibira dos parametros.
    - Un array que solo puede contener String con la palabra 'run' o 'jump'
    - Un String que represente la pista y solo puede contener '_' (suelo)
    o '|' (valla)
- La funcion imprimira com ha finalizado la carrera:
    - Si la atleta hace 'run' en '_' (suelo) y 'jump' en '|' (valla)
    sera correcto y no variara el simbolo de esa parte de la pista.
    - Si hace 'jump' en '_' (suelo), se variara la pista  por 'x'
    - Si hace 'run' en '|' (valla), se variara la pista por '/'
- La funcion retornara un boolean que infique si a superado la carrera.
Para ello tiene que realizar la opcion correcta en cada tramo de la pista.
'''


def carrera_obstaculos(acciones: list, pista: str) -> bool:

    if not isinstance(acciones, list) or not isinstance(pista, str):
        raise TypeError("Los argumentos deben ser una lista y un string")

    if not all(a in ('run', 'jump') for a in acciones):
        raise ValueError("Las acciones solo pueden contener 'run' o 'jump'")

    if not all(t in ('_', '|') for t in pista):
        raise ValueError("La pista solo puede contener '_' o '|'")

    if len(acciones) != len(pista):
        raise ValueError("La cantidad de acciones debe coincidir con la longitud de la pista")

    resultado = []
    superada  = True

    for accion, tramo in zip(acciones, pista):
        if accion == 'run' and tramo == '_':
            resultado.append('_')
        elif accion == 'jump' and tramo == '|':
            resultado.append('|')
        elif accion == 'jump' and tramo == '_':
            resultado.append('x')
            superada = False
        else:
            resultado.append('/')
            superada = False

    pista_resultado = ''.join(resultado)
    estado = "Carrera superada" if superada else "Carrera fallida"

    print(f"Pista:     {pista}")
    print(f"Resultado: {pista_resultado}")
    print(f"Estado:    {estado}")

    return superada

carrera_obstaculos(['run', 'jump', 'run', 'jump', 'run'], '_|_|_')
carrera_obstaculos(['run', 'run', 'run', 'jump', 'run'], '_|_|_')
carrera_obstaculos(['jump', 'jump', 'jump', 'jump', 'run'], '_|_|_')