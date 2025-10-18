# ----------------------------
# 1. HORARIO (TUPLA DE TUPLAS)
# ----------------------------
horario = (
    ("Lunes", "Matemática"),
    ("Martes", "Lengua"),
    ("Miércoles", "Inglés"),
    ("Jueves", "Ciencias"),
    ("Viernes", "Educación Física")
)

print(" Horario semanal:")
for dia, materia in horario:
    print(f"{dia}: {materia}")

# ----------------------------
# 2. LISTA DE COMPRAS (LISTA)
# ----------------------------
print("\n Lista de compras:")

compras = []

# Carga de productos
cantidad = int(input("¿Cuántos productos querés agregar a la lista? "))
for _ in range(cantidad):
    producto = input("Ingresá un producto: ")
    compras.append(producto.lower())

# Mostrar lista
print("\nProductos en la lista:")
for p in compras:
    print(f"- {p}")

# Contar productos
print(f"\nTotal de productos: {len(compras)}")

# Buscar producto específico
buscar = "leche"
if buscar in compras:
    print(f"Sí, '{buscar}' está en la lista.")
else:
    print(f"No, '{buscar}' no está en la lista.")

# ----------------------------
# 3. GASTOS SEMANALES (MATRIZ)
# ----------------------------
print("\n Registro de gastos semanales")

categorias = ["Comida", "Transporte", "Entretenimiento"]
gastos = []

for semana in range(4):
    print(f"\nSemana {semana + 1}:")
    fila = []
    for categoria in categorias:
        monto = float(input(f"Ingresá gasto en {categoria}: $"))
        fila.append(monto)
    gastos.append(fila)

# Gasto total por semana
print("\n Gasto total por semana:")
for i, semana in enumerate(gastos):
    total_semana = sum(semana)
    print(f"Semana {i + 1}: ${total_semana:.2f}")

# Gasto total por categoría
print("\n Gasto total por categoría:")
for j in range(3):
    total_categoria = sum(gastos[i][j] for i in range(4))
    print(f"{categorias[j]}: ${total_categoria:.2f}")

# Gasto total del mes
total_mes = sum(sum(semana) for semana in gastos)
print(f"\n Gasto total del mes: ${total_mes:.2f}")