import numpy as np

# Notas de 5 alumnos
examen1 = np.array([5.5, 7.0, 6.5, 4.0, 8.0])
examen2 = np.array([6.0, 8.5, 5.0, 6.0, 9.0])

# 1. Promedio de cada examen
prom_ex1 = np.mean(examen1)
prom_ex2 = np.mean(examen2)

print("Promedio Examen 1:", prom_ex1)
print("Promedio Examen 2:", prom_ex2)

# 2. Promedio por alumno
promedios = (examen1 + examen2) / 2
print("Promedios por alumno:", promedios)

# 3. Alumnos que aprobaron
aprobados = promedios >= 6
print("¿Quiénes aprobaron?:", aprobados)

# 4. Alumnos con mejora en el segundo examen
mejora = examen2 > examen1
print("¿Quiénes mejoraron en el segundo examen?:", mejora)
