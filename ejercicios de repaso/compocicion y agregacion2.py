class Empleado:
    def __init__(this, nombre, salario):
        this.nombre = nombre
        this.salario = salario


class Departamento:
    def __init__(this, nombre):
        this.nombre = nombre
        this.empleados = []

    def contratar_empleado(this, empleado):
        this.empleados.append(empleado)

    def despedir_empleado(this, empleado):
        this.empleados.remove(empleado)

if __name__ == "__main__":
    empleado1 = Empleado("cesar", 30000)
    empleado2 = Empleado("valentina", 40000)
    empleado3 = Empleado("Carlos", 55000)
    empleado4 = Empleado("Daniel", 65000)

    departamento = Departamento("Ventas")
    departamento.contratar_empleado(empleado1)
    departamento.contratar_empleado(empleado2)

    print("Empleados del departamento", departamento.nombre, ":")
    for empleado in departamento.empleados:
        print(empleado.nombre)

    if __name__ == "__main__":
        empleado1 = Empleado("cesar", 30000)
        empleado2 = Empleado("valentina", 40000)
        empleado3 = Empleado("Carlos", 55000)
        empleado4 = Empleado("Daniel", 65000)

    departamento = Departamento("financiero")
    departamento.contratar_empleado(empleado3)
    departamento.contratar_empleado(empleado4)

    print("Empleados del departamento", departamento.nombre, ":")
    for empleado in departamento.empleados:
        print(empleado.nombre)


