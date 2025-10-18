clientes = {}
# Función para añadir  un cliente
def agregar_cliente():
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    #Creamos un diccionario con los datos del cliente
    datos_cliente = {
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo
    }
    # Agregamos el cliente al diccionario principal
    clientes[dni] = datos_cliente
    #  Mostramos el diccionario de clientes actualizado
    print("Cliente añadido correctamente.")
    print("Base de datos actualizada:")
    print(clientes)


agregar_cliente()