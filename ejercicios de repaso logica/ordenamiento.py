def ordenamiento_por_seleccion(arreglo):
    n = len(arreglo)

    for i in range(n):

        indice_minimo = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[indice_minimo]:
                indice_minimo = j

        arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i]

if __name__ == "__main__":
    arreglo = [46, 15, 72, 82, 21]
    print("Arreglo original:", arreglo)

    ordenamiento_por_seleccion(arreglo)

    print("Arreglo ordenado:", arreglo)