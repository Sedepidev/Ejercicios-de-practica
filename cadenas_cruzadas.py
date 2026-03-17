'''
Crear una funcion que reciba dos cadenas como parametro e imprima otras dos cadenas como salida.
out1 contendra todos los caracteres de str1 que no esten en str2.
out2 contendra todos los caracteres de str2 que no esten en str1
'''


def diferencia_cadenas(str1: str, str2: str):
    set1 = set(str1)
    set2 = set(str2)

    out1 = ''.join(c for c in str1 if c not in set2)
    out2 = ''.join(c for c in str2 if c not in set1)

    print('out1: ', out1)
    print('out2: ', out2)

cadena1 = input('Escribe la primera cadena: ')
cadena2 = input('Escribe la segunda cadena: ')

diferencia_cadenas(cadena1, cadena2)