def eliminar_duplicados(arreglo):
    arreglo_sin_duplicados = []
    for elemento in arreglo:

        if elemento not in arreglo_sin_duplicados:
            arreglo_sin_duplicados.append(elemento)
    return arreglo_sin_duplicados

if __name__ == "__main__":
    arreglo = [1, 2, 3, 2, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 13, 14]
    print("Arreglo original:", arreglo)

    arreglo_sin_duplicados = eliminar_duplicados(arreglo)
    print("Arreglo sin duplicados:", arreglo_sin_duplicados)