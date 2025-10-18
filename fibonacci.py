""""Posición:     0   1   2   3   4   5   6   7   8
    Valor:        0   1   1   2   3   5   8  13  21
"""


def fibonacci(n):
    if n == 0:
        # CASO BASE 1
        return 0
    elif n == 1:
        # CASO BASE 2
        return 1
    else:
        # CASO RECURSIVO
        return fibonacci(n-2) + fibonacci(n-1)

# Pedir al usuario un número programa principal
n = int(input("Ingresá una posición: "))

# Mostrar el resultado
print("El valor en la posición", n, "es:", fibonacci(n))


