def encontrar_maximo(arreglo):
    if not arreglo:
        return None
    maximo = arreglo[0]
    for numero in arreglo:
        if numero > maximo:
            maximo = numero
    return maximo

if __name__ == "__main__":
    arreglo = [1, 7, 4, 10, 11, 6, 5]
    maximo = encontrar_maximo(arreglo)
    print("El elemento máximo en el arreglo es:", maximo)