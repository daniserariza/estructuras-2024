class CuentaBancaria:
    def __init__(object, saldo_inicial=0):
        object.__saldo = saldo_inicial

    def depositar(object, cantidad):
        if cantidad > 0:
            object.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado con éxito.")
        else:
            print("Error: La cantidad a depositar debe ser mayor que cero.")

    def retirar(object, cantidad):
        if 0 < cantidad <= object.__saldo:
            object.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado con éxito.")
        else:
            print("Error: No hay suficiente saldo para retirar esa cantidad.")

    def consultar_saldo(object):
        return object.__saldo

if __name__ == "__main__":
    cuenta = CuentaBancaria(200)

    print("Saldo actual:", cuenta.consultar_saldo())
    cuenta.depositar(800)
    print("Saldo actual:", cuenta.consultar_saldo())
    cuenta.retirar(2000)
    print("Saldo actual:", cuenta.consultar_saldo())

