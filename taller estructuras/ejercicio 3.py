def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros_str = input("Ingrese los números separados por comas: ")

numeros = [int(x) for x in numeros_str.split(',')]

resultado = suma_lista(numeros)

print("La suma de los números en la lista es:", resultado)