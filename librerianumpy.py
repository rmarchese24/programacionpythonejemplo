"""
¿Por qué usar NumPy en lugar de listas?
Mucho más rápido y eficiente con grandes volúmenes de datos.

Permite operaciones vectorizadas sin usar bucles.
Más funcionalidades matemáticas que las listas estándar de Python.

Funciones utiles
np.zeros((2,3))	Matriz de ceros 2x3
np.ones((2,3))	Matriz de unos 2x3
np.eye(3)	Matriz identidad 3x3
np.arange(0, 10, 2)	[0 2 4 6 8]
np.linspace(0, 1, 5)	5 valores entre 0 y 1
np.random.rand(3, 3)	Matriz aleatoria 3x3
np.mean () promedio o media aritmética

"""



import numpy as np

# Crear un array
a = np.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12 ]])
print("Array a:", a)

# Operaciones básicas
print("Suma:", a + 10)
print("Producto:", a * 2)
print("Media:", np.mean(a))


"""
# Crear una matriz 2x2
b = np.array([[1, 2], [3, 4]])
print("Matriz b:\n", b)

"""
