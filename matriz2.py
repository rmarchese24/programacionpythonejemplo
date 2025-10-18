def cargar_matriz(filas, columnas):
    matriz = []
    print("\nIngresá los valores de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingresá el valor en posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    print("\nMatriz ingresada:")
    for fila in matriz:
        print("\t".join(str(x) for x in fila))

def mostrar_matriz(matriz):
    print("\nMatriz ingresada:")
    for fila in matriz:
        linea = ""
        for elemento in fila:
            linea += str(elemento) + "\t"
        print(linea)

def suma_filas(matriz):
    print("\nSuma por filas:")
    for i, fila in enumerate(matriz):
        suma = sum(fila)
        print(f"Fila {i}: {suma}")

def suma_columnas(matriz):
    print("\nSuma por columnas:")
    columnas = len(matriz[0])
    for j in range(columnas):
        suma = sum(matriz[i][j] for i in range(len(matriz)))
        print(f"Columna {j}: {suma}")

def suma_total(matriz):
    total = sum(sum(fila) for fila in matriz)
    print(f"\nSuma total de todos los elementos: {total}")

# Programa principal
filas = int(input("Ingresá la cantidad de filas: "))
columnas = int(input("Ingresá la cantidad de columnas: "))

matriz = cargar_matriz(filas, columnas)
mostrar_matriz(matriz)
suma_filas(matriz)
suma_columnas(matriz)
suma_total(matriz)
