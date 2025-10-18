from collections import deque

# Pila (Stack)
pila_deque = deque()
pila_deque.append(1)
pila_deque.append(2)
pila_deque.append(3)
print("Pila (deque):", pila_deque)  # Salida: Pila (deque): deque([1, 2, 3])

elemento_sacado_pila = pila_deque.pop()
print("Elemento sacado de la pila (deque):", elemento_sacado_pila)  # Salida: Elemento sacado de la pila (deque): 3
print("Pila (deque) después de pop():", pila_deque)  # Salida: Pila (deque) después de pop(): deque([1, 2])

# Cola (Queue)
cola_deque = deque()
cola_deque.append(1)
cola_deque.append(2)
cola_deque.append(3)
print("Cola (deque):", cola_deque)  # Salida: Cola (deque): deque([1, 2, 3])

elemento_sacado_cola = cola_deque.popleft()
print("Elemento sacado de la cola (deque):", elemento_sacado_cola)  # Salida: Elemento sacado de la cola (deque): 1
print("Cola (deque) después de popleft():", cola_deque)  # Salida: Cola (deque) después de popleft(): deque([2, 3])



# Simular atención en ventanilla
cola1 = deque(["Cliente 1", "Cliente 2", "Cliente 3"])

while cola1:
    cliente = cola1.popleft()
    print(f"Atendiendo a: {cliente}")
