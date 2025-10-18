import random
import time

print("¡Bienvenido al juego Adivina el número!")
print("Estoy pensando un número del 1 al 100...")
time.sleep(2)  # pausa de 2 segundo

numero_secreto = random.randint(1, 100)
intento = None
intentos_realizados = 0

while intento != numero_secreto:
    intento = int(input(" ¿Cuál creés que es el número?: "))
    intentos_realizados += 1

    if intento < numero_secreto:
        print(" Demasiado bajo... probá con un número más alto.")
    elif intento > numero_secreto:
        print(" Demasiado alto... probá con un número más bajo.")
    else:
        print(" ¡Correcto! El número era", numero_secreto)
        print(f"Lo lograste en {intentos_realizados} intento(s).")
