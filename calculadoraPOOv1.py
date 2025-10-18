from abc import ABC, abstractmethod

# Clase abstracta
class Operacion(ABC):
    def __init__(self, numero1, numero2):
        self.__numero1 = numero1  # privado
        self.__numero2 = numero2  # privado

    def get_numero1(self):
        return self.__numero1

    def get_numero2(self):
        return self.__numero2

    @abstractmethod
    def calcular(self):
        pass


# Clases hijas concretas
class Suma(Operacion):
    def calcular(self):
        return self.get_numero1() + self.get_numero2()


class Resta(Operacion):
    def calcular(self):
        return self.get_numero1() - self.get_numero2()


class Multiplicacion(Operacion):
    def calcular(self):
        return self.get_numero1() * self.get_numero2()


class Division(Operacion):
    def calcular(self):
        if self.get_numero2() == 0:
            return "Error: división por cero"
        return self.get_numero1() / self.get_numero2()


# Calculadora: relación de agregación y asociación
class Calculadora:
    def __init__(self):
        self.historial = []  # Agregación: lista de operaciones

    def crear_operacion(self, tipo, n1, n2):
        if tipo == "suma":
            return Suma(n1, n2)
        elif tipo == "resta":
            return Resta(n1, n2)
        elif tipo == "multiplicacion":
            return Multiplicacion(n1, n2)
        elif tipo == "division":
            return Division(n1, n2)
        return None

    def realizar_operacion(self, tipo, n1, n2):
        operacion = self.crear_operacion(tipo, n1, n2)
        if operacion:
            resultado = operacion.calcular()
            self.historial.append((tipo, n1, n2, resultado))
            return resultado
        return "Operación inválida"

    def mostrar_historial(self):
        if not self.historial:
            print("No hay operaciones realizadas.")
        for i, h in enumerate(self.historial, start=1):
            print(f"{i}. {h[0]}: {h[1]} y {h[2]} = {h[3]}")


# ---- PROGRAMA PRINCIPAL ----
calc = Calculadora()

while True:
    print("\n--- CALCULADORA POO ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Ver Historial")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "6":
        print("¡Hasta luego!")
        break

    if opcion == "5":
        calc.mostrar_historial()
        continue

    n1 = float(input("Número 1: ").strip().replace(",", "."))
    n2 = float(input("Número 2: ").strip().replace(",", "."))

    if opcion == "1":
        resultado = calc.realizar_operacion("suma", n1, n2)
    elif opcion == "2":
        resultado = calc.realizar_operacion("resta", n1, n2)
    elif opcion == "3":
        resultado = calc.realizar_operacion("multiplicacion", n1, n2)
    elif opcion == "4":
        resultado = calc.realizar_operacion("division", n1, n2)
    else:
        print("Opción inválida")
        continue

    print(f"Resultado: {resultado}")
