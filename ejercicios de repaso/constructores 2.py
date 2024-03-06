class Rectangulo:
    def __init__(this, longitud, ancho):
        this.longitud = longitud
        this.ancho = ancho

    def calcular_area(this):
        return this.longitud * this.ancho

    def calcular_perimetro(this):
        return 2 * (this.longitud + this.ancho)

if __name__ == "__main__":

    rectangulo1 = Rectangulo(8, 20)
    area = rectangulo1.calcular_area()
    perimetro = rectangulo1.calcular_perimetro()

    print("Área del rectángulo:", area)
    print("Perímetro del rectángulo:", perimetro)