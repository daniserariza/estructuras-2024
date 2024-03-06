def contar_ocurrencias(arreglo):
    ocurrencias = {}
    for elemento in arreglo:
        if elemento in ocurrencias:
            ocurrencias[elemento] += 1
        else:
            ocurrencias[elemento] = 1
    return ocurrencias

if __name__ == "__main__":
    arreglo = [1, 2, 3, 4, 1, 2, 3, 1]
    resultado = contar_ocurrencias(arreglo)
    print("Ocurrencias de cada elemento:", resultado)