""" Sistema de Evaluación de Alumnos
Escribe un programa en Python que permita registrar y evaluar las calificaciones de
varios alumnos.
1. El programa debe preguntar cuántos alumnos se van a registrar .
2. Para cada alumno, debe solicitar su nombre, apellido, curso, materia y tres notas
(valores entre 0 y 10).(for o while)
3. Calcular el promedio de cada alumno usando una función.
4. Usar una estructura condicional (if) para determinar si el alumno aprueba o
reprueba (nota mínima para aprobar: 6).
5. Al final, mostrar un resumen con:
o El nombre y apellido del alumno
o Curso, materia y su promedio
o Su estado: "Aprobado" o "Reprobado"
6. Repetir este proceso usando un bucle hasta que se hayan ingresado todos los
alumnos. """

# Funcion para calcular el promedio 3)
def calcular_promedio (n1, n2, n3):
    return (n1 +n2+ n3) / 3

# Preguntar la cantidad a registrar 1)
cantidad_alumno = int(input (" ¿ Cuantos alumnos vas a registrar"))

#Bucle para ingresar los datos de cada alumno 
for  i in range (cantidad_alumno):
    #datos del alumno
    nombre = input ("NOmbre ")
    apellido = input (" Apellido")
    curso = input ("Curso")
    materia = input ("Materia")
    
    # ingreso de notas para calculo de promedio
    nota1 = float(input("Nota 1 : "))
    nota2 = float(input("Nota 2 : "))
    nota3 = float(input("Nota 3 : "))
    
    # Calcular promedio  por medio de la funcion 
    promedio = calcular_promedio (nota1, nota2, nota3)
    
    # verificar si esta aprobado o desaprobado 
    if promedio >= 6:
        estado = "Aprobado"
    else: 
        estado = "Desaprobado"
        
    # Mostrar el resultado 
    print(f"Nombre y Apellido: {nombre} {apellido}") 
    print(f"Curso: {curso} Materia: {materia} Nota: {promedio:.2f}")
    print (f"Condicion Aprobado/Desaprobado: {estado}")