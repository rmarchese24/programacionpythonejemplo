cursos = {}

def mostrar_menu():
    print("""
====== MENÚ ESCOLAR ======
1. Agregar estudiantes por curso
2. Mostrar estudiantes por curso
3. Calcular promedio general de un curso
4. Buscar estudiante por nombre
5. Salir
""")

def cargar_datos():
    curso = input("Ingresá el nombre del curso (Ej: 5A): ").upper()
    if curso not in cursos:
        cursos[curso] = []
    while True:
        nombre = input("  Nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        notas = []
        for i in range(1, 4):
            nota_valida = False
            while not nota_valida:
                nota = input(f"  Nota {i} (1 a 10): ")
                if nota.isdigit():
                    nota = int(nota)
                    if 1 <= nota <= 10:
                        notas.append(nota)
                        nota_valida = True
                    else:
                        print("  ❌ La nota debe estar entre 1 y 10.")
                else:
                    print("  ❌ Ingresá solo números enteros.")
        estudiante = (nombre, tuple(notas))
        cursos[curso].append(estudiante)

def mostrar_estudiantes():
    if not cursos:
        print("No hay cursos cargados.")
        return
    for curso, lista in cursos.items():
        print(f"\n📘 Curso {curso}:")
        for nombre, notas in lista:
            print(f"  - {nombre} → Notas: {notas}")

def promedio_general():
    curso = input("Ingresá el curso para calcular promedio: ").upper()
    if curso in cursos and len(cursos[curso]) > 0:
        total = 0
        cantidad = 0
        for _, notas in cursos[curso]:
            total += sum(notas)
            cantidad += len(notas)
        promedio = total / cantidad
        print(f"📊 Promedio general del curso {curso}: {promedio:.2f}")
    else:
        print("❌ Curso no encontrado o sin estudiantes.")

def buscar_estudiante():
    nombre_buscado = input("Ingresá el nombre del estudiante a buscar: ").lower()
    encontrado = False
    for curso, lista in cursos.items():
        for nombre, notas in lista:
            if nombre.lower() == nombre_buscado:
                print(f"✅ {nombre} está en el curso {curso} → Notas: {notas}")
                encontrado = True
    if not encontrado:
        print("❌ Estudiante no encontrado.")

# Programa principal sin main y sin try
opcion = ''
while opcion != '5':
    mostrar_menu()
    opcion = input("Seleccioná una opción: ")

    if opcion == '1':
        cargar_datos()
    elif opcion == '2':
        mostrar_estudiantes()
    elif opcion == '3':
        promedio_general()
    elif opcion == '4':
        buscar_estudiante()
    elif opcion == '5':
        print("👋 Fin del programa.")
    else:
        print("❌ Opción inválida.")
