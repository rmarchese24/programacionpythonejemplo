# agenda.py

agenda = {}

def añadir_modificar(dni):
    if dni in agenda:
        print("Contacto encontrado:")
        mostrar_contacto(dni)
        opcion = input("¿Deseás modificar los datos? (s/n): ").lower()
        if opcion != 's':
            return
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    edad = int(input("Edad: "))

    agenda[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
        "edad": edad
    }
    print("Contacto guardado/modificado.")

def buscar_por_nombre(cadena):
    print(f"Contactos que comienzan con '{cadena}':")
    encontrados = False
    for dni, datos in agenda.items():
        nombre_completo = datos["nombre"].lower() + " " + datos["apellido"].lower()
        if nombre_completo.startswith(cadena.lower()):
            mostrar_contacto(dni)
            encontrados = True
    if not encontrados:
        print("No se encontraron contactos.")

def borrar_por_nombre(nombre):
    encontrados = []
    for dni, datos in agenda.items():
        if datos["nombre"].lower() == nombre.lower():
            encontrados.append(dni)
    
    if not encontrados:
        print("No se encontraron contactos con ese nombre.")
        return

    for dni in encontrados:
        mostrar_contacto(dni)
        confirmar = input(f"¿Deseás borrar este contacto (DNI: {dni})? (s/n): ").lower()
        if confirmar == 's':
            del agenda[dni]
            print("Contacto borrado.")

def listar_contactos():
    if not agenda:
        print("La agenda está vacía.")
        return
    print("Contactos en la agenda:")
    for dni in agenda:
        mostrar_contacto(dni)

def mostrar_edades_potencia():
    if not agenda:
        print("La agenda está vacía.")
        return
    try:
        potencia = int(input("¿A qué potencia deseas elevar las edades?: "))
    except ValueError:
        print("Ingresá un número válido.")
        return
    print(f"Edades elevadas a la potencia {potencia}:")
    for datos in agenda.values():
        edad = datos["edad"]
        print(f"{datos['nombre']} {datos['apellido']}: {edad ** potencia}")

def mostrar_contacto(dni):
    datos = agenda[dni]
    print(f"DNI: {dni} | {datos['nombre']} {datos['apellido']} | Tel: {datos['telefono']} | Email: {datos['email']} | Edad: {datos['edad']}")
