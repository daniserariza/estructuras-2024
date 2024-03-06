def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if columnas_matriz1 != filas_matriz2:
        return None
    resultado = [[0 for _ in range(columnas_matriz2)] for _ in range(filas_matriz1)]

    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(filas_matriz2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

if __name__ == "__main__":
    matriz1 = [[1, 2, 3],
               [4, 5, 6]]

    matriz2 = [[7, 8],
               [9, 10],
               [11, 12]]

    resultado = multiplicar_matrices(matriz1, matriz2)
    if resultado is not None:
        print("Resultado de la multiplicación de matrices:")
        for fila in resultado:
            print(fila)
    else:
        print("Las dimensiones de las matrices no son adecuadas para la multiplicación.")