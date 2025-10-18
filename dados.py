import random
import time
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Suma: {suma}")
    return dado1, dado2

# Programa principal
contador_lanzamientos = 0
contador_dobles = 0


while True:
    input("Presioná Enter para lanzar los dados...")
    time.sleep(2)  # pausa de 2 segundo
    d1, d2 = lanzar_dados()
    contador_lanzamientos += 1
    
    if d1 == d2:
        contador_dobles += 1
        print("¡Sacaste un doble!")

    opcion = input("¿Querés volver a lanzar? (s/n): ").lower()
    if opcion != "s":
        break

print("\n Resumen:")
print(f"Total de lanzamientos: {contador_lanzamientos}")
print(f"Cantidad de dobles: {contador_dobles}")
print("¡Gracias por jugar!")
