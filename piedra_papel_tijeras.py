'''
Un programa que calcuole quien gana mas partidas al piedra,
papel, tijeras.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate).
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "R" (piedra), "P" (papel)
o "S" (tijera).
- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
'''


def piedra_papel_tijeras(partidas: list) -> str:
    if not isinstance(partidas, list):
        raise TypeError("El argumento debe ser una lista")

    jugadas_validas = ('R', 'P', 'S')

    for partida in partidas:
        if not isinstance(partida, tuple) or len(partida) != 2:
            raise TypeError("Cada partida debe ser una tupla de 2 elementos")
        if partida[0] not in jugadas_validas or partida[1] not in jugadas_validas:
            raise ValueError("Las jugadas solo pueden ser 'R', 'P' o 'S'")

    gana_a = {
        'R': 'S',
        'P': 'R',
        'S': 'P'
    }
    victorias_p1 = 0
    victorias_p2 = 0

    for jugada_p1, jugada_p2 in partidas:
        if jugada_p1 == jugada_p2:
            continue
        elif gana_a[jugada_p1] == jugada_p2:
            victorias_p1 += 1
        else:
            victorias_p2 += 1

    if victorias_p1 > victorias_p2:
        return "Player 1"
    elif victorias_p2 > victorias_p1:
        return "Player 2"
    else:
        return "Tie"

print(piedra_papel_tijeras([("R", "S"), ("S", "R"), ("P", "S")]))
print(piedra_papel_tijeras([("R", "S"), ("P", "R"), ("S", "P")]))
print(piedra_papel_tijeras([("R", "S"), ("S", "P"), ("P", "R")]))
print(piedra_papel_tijeras([("R", "R"), ("P", "P"), ("S", "S")]))
print(piedra_papel_tijeras([("R", "P")]))