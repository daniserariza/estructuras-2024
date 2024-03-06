def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    pivote = arreglo[len(arreglo) // 2]
    izquierda = [x for x in arreglo if x < pivote]
    medio = [x for x in arreglo if x == pivote]
    derecha = [x for x in arreglo if x > pivote]

    return quicksort(izquierda) + medio + quicksort(derecha)


if __name__ == "__main__":
    arreglo = [3, 6, 8, 10, 1, 2, 1]
    print("Arreglo original:", arreglo)

    arreglo_ordenado = quicksort(arreglo)
    print("Arreglo ordenado:", arreglo_ordenado)