class Persona:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero

if __name__ == "__main__":

    persona1 = Persona("Hernesto ", "Roa", 30,"masculino")

    print("Nombre:", persona1.obtener_nombre())
    print("Apellido:",persona1.obtener_apellido())
    print("Edad:", persona1.obtener_edad())
    print("Género:", persona1.obtener_genero())
    