'''
Crea una funcion que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscara y retornara los elementos comunes
de los dos array.
- Si el boolenao es falso buscara y retornara los elementos no comunes
de los dos array
- No se pueden utilizar operaciones del lenguaje que lo resuelvan
directamente.
'''


def comparar_arrays(arr1: list, arr2: list, comunes: bool) -> list:
    
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Los dos primeros argumentos deben ser listas")
    if not isinstance(comunes, bool):
        raise TypeError("El tercer argumento debe ser un booleano")

    def esta_en(elemento, array: list) -> bool:
        for item in array:
            if item == elemento:
                return True
        return False

    def agregar_si_no_existe(elemento, array: list) -> None:
        if not esta_en(elemento, array):
            array.append(elemento)

    resultado = []

    if comunes:
        for elemento in arr1:
            if esta_en(elemento, arr2):
                agregar_si_no_existe(elemento, resultado)
    else:
        for elemento in arr1:
            if not esta_en(elemento, arr2):
                agregar_si_no_existe(elemento, resultado)
        for elemento in arr2:
            if not esta_en(elemento, arr1):
                agregar_si_no_existe(elemento, resultado)

    return resultado

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

print(comparar_arrays(arr1, arr2, True))
print(comparar_arrays(arr1, arr2, False))

arr3 = ['a', 'b', 'c', 'd']
arr4 = ['c', 'd', 'e', 'f']

print(comparar_arrays(arr3, arr4, True))
print(comparar_arrays(arr3, arr4, False))

print(comparar_arrays([1, 2, 2, 3], [2, 3, 3, 4], True))
print(comparar_arrays([1, 2, 2, 3], [2, 3, 3, 4], False))