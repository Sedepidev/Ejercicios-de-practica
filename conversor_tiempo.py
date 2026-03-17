'''
Crea una funcion que reciba dias, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.
'''


def a_milisegundos(dias: int = 0, horas: int = 0, minutos: int = 0, segundos: int = 0) -> int:
    argumentos = {'dias': dias, 'horas': horas, 'minutos': minutos, 'segundos': segundos}

    for nombre, valor in argumentos.items():
        if not isinstance(valor, int):
            raise TypeError(f"'{nombre}' debe ser un entero, se recibió {type(valor).__name__}")
        if valor < 0:
            raise ValueError(f"'{nombre}' no puede ser negativo")

    MS_POR_SEGUNDO = 1_000
    MS_POR_MINUTO  = 60 * MS_POR_SEGUNDO
    MS_POR_HORA    = 60 * MS_POR_MINUTO
    MS_POR_DIA     = 24 * MS_POR_HORA

    return (dias * MS_POR_DIA +
            horas * MS_POR_HORA +
            minutos * MS_POR_MINUTO +
            segundos * MS_POR_SEGUNDO)

print(a_milisegundos(segundos=1))
print(a_milisegundos(minutos=1))
print(a_milisegundos(horas=1))
print(a_milisegundos(dias=1))
print(a_milisegundos(1, 2, 30, 15))