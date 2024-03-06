lista = []

def agregar_elemento():
    while True:
        elemento = input("Introduce un elemento para agregar a la lista (o 'fin' para terminar): ")
        if elemento.lower() == 'fin':
            break
        lista.append(elemento)

agregar_elemento()
print("Lista final:", lista)
