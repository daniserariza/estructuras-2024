class Coche:
    def __init__(this):
        this.__velocidad = 0

    def acelerar(this, incremento):
        if incremento > 0:
            this.__velocidad += incremento
            print(f"Acelerando. Velocidad actual: {this.__velocidad} km/h")
        else:
            print("Error: El incremento de velocidad debe ser mayor que cero.")

    def frenar(this, decremento):
        if 0 < decremento <= this.__velocidad:
            this.__velocidad -= decremento
            print(f"Frenando. Velocidad actual: {this.__velocidad} km/h")
        else:
            print("Error: No se puede frenar más de lo que ya se está detenido.")

    def obtener_velocidad(this):
        return this.__velocidad

if __name__ == "__main__":
    coche = Coche()

    print("Velocidad actual:", coche.obtener_velocidad())
    coche.acelerar(80)
    coche.frenar(40)
    coche.acelerar(20)