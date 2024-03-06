def suma_arreglo(arreglo):
    suma = 0
    for numero in arreglo:
        suma += numero
    return suma

if __name__ == "__main__":
    arreglo = [1, 2, 3, 4, 5]
    resultado = suma_arreglo(arreglo)
    print("La suma de los elementos del arreglo es:", resultado)