# Pila (Stack)
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print("Pila:", pila)  # Salida: Pila: [1, 2, 3]

elemento_sacado = pila.pop()
print("Elemento sacado de la pila:", elemento_sacado)  # Salida: Elemento sacado de la pila: 3
print("Pila después de pop:", pila)  # Salida: Pila después de pop: [1, 2]

# Cola (Queue)
cola = []
cola.append(1)
cola.append(2)
cola.append(3)
print("Cola:", cola)  # Salida: Cola: [1, 2, 3]

elemento_sacado = cola.pop(0)
print("Elemento sacado de la cola:", elemento_sacado)  # Salida: Elemento sacado de la cola: 1
print("Cola después de pop(0):", cola)  # Salida: Cola: [2, 3]