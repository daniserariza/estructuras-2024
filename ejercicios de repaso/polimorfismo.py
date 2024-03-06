class Persona:
    def __init__(object, nombre):
        object.nombre = nombre

    def saludar(object):
        print(f"Hola, soy {object.nombre}. ¡Un placer conocerte!")

class Empleado(Persona):
    def __init__(object, nombre, trabajo):
        super().__init__(nombre)
        object.trabajo = trabajo

    def saludar(object):
        print(f"Hola, soy {object.nombre} y trabajo como {object.trabajo}.")

class Estudiante(Persona):
    def __init__(object, nombre, semestre):
        super().__init__(nombre)
        object.semestre = semestre

    def saludar(object):
        print(f"Hola, soy {object.nombre} y estoy en el {object.semestre} semestre.")


juan = Empleado(nombre="ariel", trabajo="vigilante")
ana = Estudiante(nombre="daniela", semestre="primer")

juan.saludar()
ana.saludar()