def buscar_numero(arreglo, objetivo):
    for numero in arreglo:
        if numero == objetivo:
            return True
    return False

if __name__ == "__main__":
    arreglo = [1, 3, 5, 7, 9]
    objetivo = 4
    resultado = buscar_numero(arreglo, objetivo)
    print(f"El número {objetivo} está presente en el arreglo {resultado}")