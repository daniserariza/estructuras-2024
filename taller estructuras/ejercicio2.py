def eliminar_duplicados(lista):

    lista_sin_duplicados = []

    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

mi_lista = [1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8,9]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
print("Lista original:", mi_lista)
print("Lista sin duplicados:", lista_sin_duplicados)
