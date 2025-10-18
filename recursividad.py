#con recursividad

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Programa principal Ejemplo de uso
numero = 5
print("Factorial recursivo:", factorial_recursivo(numero))  # Resultado: 120

def factorial(n):
    if n == 0 or n == 1:      # 🟩 CASO BASE
        return 1
    else:                     # 🔁 REGLA RECURSIVA
        return n * factorial(n - 1)


# sin recursividad
def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
numero = 5
print("Factorial iterativo:", factorial_iterativo(numero))  # Resultado: 120

# sumar elementos de una lista
#recursividad
def suma_lista_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista_recursiva(lista[1:]) 
    #Devuelve una nueva lista que contiene todos los elementos excepto el primero.

# Ejemplo de uso
numeros = [4, 7, 2, 9]
print("Suma recursiva:", suma_lista_recursiva(numeros))  # Resultado: 22

# sin recursividad
def suma_lista_iterativa(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso
numeros = [4, 7, 2, 9]
print("Suma iterativa:", suma_lista_iterativa(numeros))  # Resultado: 22

# Cuenta regresiva
def cuenta_regresiva(n):
    if n == 0:
        print("¡Despegue! ")
    else:
        print(f"{n}...")
        cuenta_regresiva(n - 1)

# Ejemplo de uso
cuenta_regresiva(5)

def cuenta_regresiva(n):
    if n == 0:
        print("¡Despegue! ")   # 🟩 CASO BASE
    else:
        print(f"{n}...")         # 🔁 REGLA RECURSIVA
        cuenta_regresiva(n - 1)  # 🔁 LLAMADA RECURSIVA



# sin recursividad con bucle 
def cuenta_regresiva_iterativa(n):
    while n > 0:
        print(f"{n}...")
        n -= 1
    print("¡Despegue! ")

# Ejemplo de uso
cuenta_regresiva_iterativa(5)

