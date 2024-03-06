class Persona:
    def __init__(this, nombre, edad,):
        this.nombre = nombre
        this.edad = edad

class Estudiante(Persona):
    def __init__(this, nombre, edad, semestre, universidad):
        super().__init__(nombre, edad)
        this.semestre = semestre
        this.universidad = universidad

andres = Estudiante(nombre="andres", edad=21, semestre="3", universidad="udecaldas")
print(f"{andres.nombre} de {andres.edad} años de edad es un estudiante de {andres.semestre} semestre de la {andres.universidad}.")