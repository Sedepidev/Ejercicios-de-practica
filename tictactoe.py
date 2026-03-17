'''
Crea una funcion que analice una matriz 3x3 compuesto por 'X' y 'O'
y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.
'''


def analizar_tictactoe(matriz: list) -> str:

    if not isinstance(matriz, list) or len(matriz) != 3:
        return "Nulo"

    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != 3:
            return "Nulo"
        if not all(celda in ('X', 'O', '') for celda in fila):
            return "Nulo"


    total_x = sum(fila.count('X') for fila in matriz)
    total_o = sum(fila.count('O') for fila in matriz)

    if abs(total_x - total_o) > 1 or total_o > total_x:
        return "Nulo"

    lineas = [
        # Filas
        [matriz[0][0], matriz[0][1], matriz[0][2]],
        [matriz[1][0], matriz[1][1], matriz[1][2]],
        [matriz[2][0], matriz[2][1], matriz[2][2]],
        
        # Columnas
        [matriz[0][0], matriz[1][0], matriz[2][0]],
        [matriz[0][1], matriz[1][1], matriz[2][1]],
        [matriz[0][2], matriz[1][2], matriz[2][2]],
        
        # Diagonales
        [matriz[0][0], matriz[1][1], matriz[2][2]],
        [matriz[0][2], matriz[1][1], matriz[2][0]],
    ]

    def tiene_linea(jugador: str) -> bool:
        return any(all(celda == jugador for celda in linea) for linea in lineas)

    gana_x = tiene_linea('X')
    gana_o = tiene_linea('O')

    if gana_x and gana_o:
        return "Nulo"
    if gana_x:
        return "X"
    if gana_o:
        return "O"

    hay_vacios = any(celda == '' for fila in matriz for celda in fila)
    return "Nulo" if hay_vacios else "Empate"

print(analizar_tictactoe([['X', 'X', 'X'],
                          ['O', 'O', '' ],
                          ['' , '' , '' ]]))

print(analizar_tictactoe([['O', 'X', 'X'],
                          ['X', 'O', '' ],
                          ['' , '' , 'O']]))

print(analizar_tictactoe([['X', 'O', 'X'],
                          ['X', 'X', 'O'],
                          ['O', 'X', 'O']]))

print(analizar_tictactoe([['X', 'X', 'X'],
                          ['X', 'O', '' ],
                          ['' , '' , '' ]]))

print(analizar_tictactoe([['X', 'X', 'X'],
                          ['O', 'O', 'O'],
                          ['' , '' , '' ]]))

print(analizar_tictactoe([['X', 'O', '' ],
                          ['' , 'X', '' ],
                          ['' , '' , '' ]]))