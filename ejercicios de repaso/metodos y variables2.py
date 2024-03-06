class Empleado:
    empleados = []

    def __init__(object, nombre, salario):
        object.nombre = nombre
        object.salario = salario
        Empleado.empleados.append(object)

    def calcular_salario_promedio():
        total_salarios = sum(empleado.salario for empleado in Empleado.empleados)
        return total_salarios / len(Empleado.empleados) if Empleado.empleados else 0

    calcular_salario_promedio = staticmethod(calcular_salario_promedio)

if __name__ == "__main__":
    empleado1 = Empleado("sergio", 400000)
    empleado2 = Empleado("gloria", 300000)
    empleado3 = Empleado("teresa", 350000)

    print("Salario promedio de todos los empleados:", Empleado.calcular_salario_promedio())