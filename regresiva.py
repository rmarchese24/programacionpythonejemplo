def cuenta_regresiva(n):
    if n == 0:
        print("¡Despegue! ")   # 🟩 CASO BASE
    else:
        print(f"{n}...")         # 🔁 REGLA RECURSIVA
        cuenta_regresiva(n - 1)  # 🔁 LLAMADA RECURSIVA

# programa
cuenta_regresiva(10)

