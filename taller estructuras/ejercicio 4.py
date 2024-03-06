def tienen_elemento_en_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]
lista_c =  [1, 3, 9, 6, 5]

if tienen_elemento_en_comun(lista_a, lista_b):
    print("Las listas tienen al menos un elemento en común.")
else:
    print("Las listas no tienen elementos en común.")