'''
Crea una funcion que sume 2 numeros y retorne su resultado pasados
unos segundos,
- Recibira por parametros los 2 numeros a sumar y los segundos
que debe tardar en finalizar su ejecucion.
- Debera retornar el resultado de forma asincrona, es decir, sin detener
la ejecucion del programa principal.
Se podria ejecutar varias veces al mismo tiempo.
'''


import asyncio

async def suma_asincrona(a: float, b: float, segundos: float) -> float:
    await asyncio.sleep(segundos)
    return a + b

async def main():
    tarea1 = asyncio.create_task(suma_asincrona(2, 3, 3))
    tarea2 = asyncio.create_task(suma_asincrona(13, 5, 1))
    tarea3 = asyncio.create_task(suma_asincrona(7, 7, 2))

    print('Tareas ejecutandose, el programa sigue en proceso...')

    print('Tarea 2: 10 + 5 = ', await tarea2)
    print('Tarea 3: 7 + 7 = ', await tarea3)
    print('Tarea 1: 2 + 3 = ', await tarea1)

asyncio.run(main())