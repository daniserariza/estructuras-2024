def fibonacci_iterativo(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    fib_ant1 = 0
    fib_ant2 = 1
    fib_actual = 0

    for i in range(2, n):
        fib_actual = fib_ant1 + fib_ant2
        fib_ant1, fib_ant2 = fib_ant2, fib_actual

    return fib_actual

if __name__ == "__main__":
    n = 10
    resultado = fibonacci_iterativo(n)
    print(f"El término {n} de la secuencia de Fibonacci es: {resultado}")
