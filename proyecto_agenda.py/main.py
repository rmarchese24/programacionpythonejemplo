# main.py

import agenda

def mostrar_menu():
    print("\n--- MENÚ DE AGENDA ---")
    print("1. Añadir/Modificar contacto")
    print("2. Buscar por nombre/apellido")
    print("3. Borrar contacto por nombre")
    print("4. Listar todos los contactos")
    print("5. Mostrar edades elevadas a potencia")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            dni = input("Ingresá el DNI: ")
            agenda.añadir_modificar(dni)
        elif opcion == "2":
            cadena = input("Buscar nombres que comiencen con: ")
            agenda.buscar_por_nombre(cadena)
        elif opcion == "3":
            nombre = input("Ingresá el nombre del contacto a borrar: ")
            agenda.borrar_por_nombre(nombre)
        elif opcion == "4":
            agenda.listar_contactos()
        elif opcion == "5":
            agenda.mostrar_edades_potencia()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()
