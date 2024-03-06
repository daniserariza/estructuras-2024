class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, nueva_edad):
        self.edad = nueva_edad

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, nuevo_genero):
        self.genero = nuevo_genero


if __name__ == "__main__":

    persona1 = Persona("sergio", 21, "Masculino")

    print("Nombre:", persona1.obtener_nombre())
    print("Edad:", persona1.obtener_edad())
    print("Género:", persona1.obtener_genero())

    persona1.establecer_nombre("daniela")
    persona1.establecer_edad(20)
    persona1.establecer_genero("Femenino")

    print("Nuevo nombre:", persona1.obtener_nombre())
    print("Nueva edad:", persona1.obtener_edad())
    print("Nuevo género:", persona1.obtener_genero())
