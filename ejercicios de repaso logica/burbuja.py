def ordenamiento_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

if __name__ == "__main__":
    arreglo = [65, 34, 26, 13, 42, 31, 10]
    print("Arreglo original:", arreglo)

    ordenamiento_burbuja(arreglo)

    print("Arreglo ordenado:", arreglo)