class Motor:
    def __init__(object, tipo, cilindros):
        object.tipo = tipo
        object.cilindros = cilindros

    def arrancar(object):
        print("¡El motor arrancó!")


class Coche:
    def __init__(object, marca, modelo, color, tipo_motor, cilindros):
        object.marca = marca
        object.modelo = modelo
        object.color = color
        object.motor = Motor(tipo_motor, cilindros)

    def arrancar(object):
        print(f"Arranco el coche {object.marca} {object.modelo}...")
        object.motor.arrancar()

if __name__ == "__main__":
    coche1 = Coche("Toyota", "Prado", "Negra", "Dieesel", 8)
    coche2 = Coche("Nissan", "March", "Blanco", "Gasolina", 4)

    coche1.arrancar()
    coche2.arrancar()