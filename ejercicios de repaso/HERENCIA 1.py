class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad


class Empleado(Persona):
    def __init__(self, nombre, edad, salario, puesto):
        Persona.__init__(self, nombre, edad)
        self.salario = salario
        self.puesto = puesto

    def obtener_salario(self):
        return self.salario

    def obtener_puesto(self):
        return self.puesto

if __name__ == "__main__":
    # Crear una instancia de Empleado
    empleado1 =  Empleado("carlos", 30,1850000,"jefe")
    print("Nombre:", empleado1.obtener_nombre())
    print("Edad:", empleado1.obtener_edad())

    print("Salario:", empleado1.obtener_salario())
    print("Puesto:", empleado1.obtener_puesto())
