'''
La idea es crear un programa que calcule la diferencia de dias entre dos
cadenas de texto que representen fechas.
Tienen que tener el formato dd/mm/aaaa.
La funcion recibe dos strings y retorna un int.
La diferencia de los dias siempre sera absoluta.
Si una de las dos cadenas de texto no representa una fecha valida, se lanzara
una excepcion.
'''


import datetime

def dias_restantes(fecha1: str, fecha2: str) -> int:
    
    if not isinstance(fecha1, str) or not isinstance(fecha2,str):
        raise TypeError('Ambos argumentos deben de ser strings')
    
    formato = '%d/%m/%Y'
    try:
        fecha1 = datetime.datetime.strptime(fecha1, formato)
        fecha2 = datetime.datetime.strptime(fecha2, formato)
    except ValueError:
        raise ValueError('La fecha no es valida, debe estar en el formato dd/mm/aaaa')
    return abs((fecha1 - fecha2).days)

print(dias_restantes("01/01/2024", "31/12/2024"))
print(dias_restantes("31/12/2024", "01/01/2024"))
print(dias_restantes("15/06/2023", "15/06/2023"))