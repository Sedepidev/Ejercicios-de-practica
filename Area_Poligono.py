'''
El objetivo es crear una funcion que sea capaz de calcular el area de un poligono.
Para este ejercicio seran solo triangulo, cuadrado y rectangulo.
Se puede escalar facilmente haciendo las formulas de mas poligonos.
'''

def poligonos(altura, base, cantidad):
    if cantidad < 3:
        print("Esto no es un poligono.")
    elif altura == base and cantidad == 4:
        area_cuadrado = altura * 2
        print("El area del cuadrado es: ", area_cuadrado)
    elif cantidad == 4:
        area_rectangulo = altura * base
        print("El area del rectangulo es: ", area_rectangulo)
    elif cantidad == 3:
        area_triangulo = altura * base / 2
        print("El area del triangulo es: ", area_triangulo)
    else:
        print("Esto no estaba contemplado.")

poligonos(4, 4, 4)
poligonos(2, 4, 4)
poligonos(4, 4, 3)
poligonos(2, 4, 2)
poligonos(2, 2, 5)