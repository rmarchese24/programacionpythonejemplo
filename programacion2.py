# Función para calcular el promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Preguntar cuántos alumnos se van a registrar
cantidad_alumnos = int(input("¿Cuántos alumnos desea registrar? "))

# Lista para guardar la información de cada alumno
alumnos = []

# Contador de alumnos
i = 0
while i < cantidad_alumnos:
    print(f"\n--- Registro del alumno {i + 1} ---")
    nombre = input("Nombre: ").strip().capitalize()
    apellido = input("Apellido: ").strip().capitalize()
    curso = input("Curso: ").strip()
    materia = input("Materia: ").strip()

    # Ingresar tres notas
    notas = []
    j = 0
    while j < 3:
        nota = float(input(f"Ingrese la nota {j + 1} (0-10): ").replace(",", "."))
        if 0 <= nota <= 10:
            notas.append(nota)
            j += 1
        else:
            print("⚠️ La nota debe estar entre 0 y 10. Intente de nuevo.")

    # Calcular promedio
    promedio = calcular_promedio(notas)

    # Determinar estado
    if promedio >= 6:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    # Guardar datos del alumno
    alumnos.append({
        "nombre": nombre,
        "apellido": apellido,
        "curso": curso,
        "materia": materia,
        "promedio": promedio,
        "estado": estado
    })

    i += 1  # Pasar al siguiente alumno

# Mostrar resumen
print("\n===== RESUMEN DE ALUMNOS =====")
k = 0
while k < len(alumnos):
    alumno = alumnos[k]
    print(f"\nAlumno: {alumno['nombre']} {alumno['apellido']}")
    print(f"Curso: {alumno['curso']} | Materia: {alumno['materia']}")
    print(f"Promedio: {alumno['promedio']:.2f}")
    print(f"Estado: {alumno['estado']}")
    k += 1
