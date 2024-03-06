class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)



if __name__ == "__main__":

    rectangulo1 = Rectangulo(10, 12)

    area = rectangulo1.calcular_area()
    perimetro = rectangulo1.calcular_perimetro()

    print("Área del rectángulo:", area)
    print("Perímetro del rectángulo:", perimetro)