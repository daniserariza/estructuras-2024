class FiguraGeometrica:
    def calcular_area(object):
        pass

    def calcular_perimetro(object):
        pass


class Rectangulo(FiguraGeometrica):
    def __init__(object, longitud, ancho):
        object.longitud = longitud
        object.ancho = ancho

    def calcular_area(object):
        return object.longitud * object.ancho

    def calcular_perimetro(object):
        return 2 * (object.longitud + object.ancho)


class Circulo(FiguraGeometrica):
    def __init__(object, radio):
        object.radio = radio

    def calcular_area(object):
        return 3.14 * object.radio ** 2

    def calcular_perimetro(object):
        return 2 * 3.14 * object.radio

if __name__ == "__main__":
    rectangulo = Rectangulo(5, 4)
    print("Rectángulo:")
    print("Área:", rectangulo.calcular_area())
    print("Perímetro:", rectangulo.calcular_perimetro())

    circulo = Circulo(3)
    print("\nCírculo:")
    print("Área:", circulo.calcular_area())
    print("Perímetro:", circulo.calcular_perimetro())