def encontrar_subcadena(cadena, subcadena):
    if subcadena not in cadena:
        return -1
    else:
        return cadena.index(subcadena)

if __name__ == "__main__":
    cadena = "hoy tengo clase en la universidad"
    subcadena = "universidad"
    posicion = encontrar_subcadena(cadena, subcadena)

    if posicion != -1:
        print(f"La subcadena '{subcadena}' se encuentra en la posición {posicion} de la cadena.")
    else:
        print(f"La subcadena '{subcadena}' no se encuentra en la cadena.")