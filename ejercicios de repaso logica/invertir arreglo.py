def invertir_arreglo(arreglo):
    longitud = len(arreglo)
    for i in range(longitud // 2):

        arreglo[i], arreglo[longitud - 1 - i] = arreglo[longitud - 1 - i], arreglo[i]

if __name__ == "__main__":
    arreglo = [1, 2, 3, 4, 5]
    print("Arreglo original:", arreglo)

    invertir_arreglo(arreglo)
    print("Arreglo invertido:", arreglo)