def multiplicacion_matriz(matriz):
    resultado = 1
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            resultado *= matriz[i][j]

    return resultado

mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
]
resultado_multiplicacion = multiplicacion_matriz(mi_matriz)

print("La multiplicación de los elementos de la matriz es:", resultado_multiplicacion)