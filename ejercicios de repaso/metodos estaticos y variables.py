class Persona:
    contador = 0

    def __init__(self, nombre,apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        Persona.contador += 1

    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero


    def obtener_total_personas(self):
        return self.contador


if __name__ == "__main__":
    persona1 = Persona("Julian", "perez", 23,"Masculino")
    persona2 = Persona("juana", "galvez", 21, "Femenino")
    persona3 = Persona("Carlos", "ariza", 29,"Masculino")

    print("Total de personas creadas:", persona1.obtener_total_personas())