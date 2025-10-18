from abc import ABC, abstractmethod
import math

# ============
#  POO: MODELO
# ============

class Operacion(ABC):
    """Clase abstracta que representa una operación."""
    def __init__(self, numero1, numero2=None):
        self.__numero1 = None
        self.__numero2 = None
        self.set_numero1(numero1)
        if numero2 is not None:
            self.set_numero2(numero2)

    # Encapsulamiento: getters/setters
    def get_numero1(self):
        return self.__numero1

    def set_numero1(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("numero1 debe ser numérico")
        self.__numero1 = float(valor)

    def get_numero2(self):
        return self.__numero2

    def set_numero2(self, valor):
        if valor is None:
            self.__numero2 = None
            return
        if not isinstance(valor, (int, float)):
            raise TypeError("numero2 debe ser numérico")
        self.__numero2 = float(valor)

    @abstractmethod
    def calcular(self):
        pass

    @abstractmethod
    def nombre(self):
        pass

    def __str__(self):
        n1 = self.get_numero1()
        n2 = self.get_numero2()
        resultado = self.calcular()
        s_args = f"{n1}" + (f", {n2}" if n2 is not None else "")
        return f"{self.nombre()}({s_args}) = {resultado}"


# -------------------
# Operaciones binarias
# -------------------
class Suma(Operacion):
    def calcular(self):
        return self.get_numero1() + (self.get_numero2() or 0.0)

    def nombre(self):
        return "Suma"


class Resta(Operacion):
    def calcular(self):
        return self.get_numero1() - self.get_numero2()

    def nombre(self):
        return "Resta"


class Multiplicacion(Operacion):
    def calcular(self):
        return self.get_numero1() * self.get_numero2()

    def nombre(self):
        return "Multiplicación"


class Division(Operacion):
    def calcular(self):
        return self.get_numero1() / self.get_numero2()

    def nombre(self):
        return "División"


class Potencia(Operacion):
    def calcular(self):
        return self.get_numero1() ** self.get_numero2()

    def nombre(self):
        return "Potencia"


# ------------------
# Operaciones unarias
# ------------------
class RaizCuadrada(Operacion):
    def __init__(self, numero):
        super().__init__(numero, None)

    def calcular(self):
        return math.sqrt(self.get_numero1())

    def nombre(self):
        return "Raíz Cuadrada"


class Logaritmo(Operacion):
    def __init__(self, numero, base=math.e):
        super().__init__(numero, base)

    def calcular(self):
        return math.log(self.get_numero1(), self.get_numero2())

    def nombre(self):
        return "Logaritmo"


# ==================
#   CALCULADORA
# ==================
class Calculadora:
    def __init__(self):
        self.__historial = []

    def get_historial(self):
        return list(self.__historial)

    def _registrar(self, op):
        self.__historial.append(op)
        return op.calcular()

    def realizar_operacion(self, tipo, n1, n2=None):
        tipo = tipo.lower().strip()
        operaciones = {
            "suma": Suma,
            "resta": Resta,
            "multiplicacion": Multiplicacion,
            "multiplicación": Multiplicacion,
            "division": Division,
            "división": Division,
            "potencia": Potencia,
            "raiz": RaizCuadrada,
            "raíz": RaizCuadrada,
            "log": Logaritmo,
            "logaritmo": Logaritmo
        }

        if tipo in ["raiz", "raíz"]:
            op = RaizCuadrada(n1)
            return self._registrar(op)
        elif tipo in ["log", "logaritmo"]:
            op = Logaritmo(n1, n2 if n2 is not None else math.e)
            return self._registrar(op)
        elif tipo in operaciones:
            op = operaciones[tipo](n1, n2)
            return self._registrar(op)

        raise ValueError(f"Operación no soportada: '{tipo}'")


class CalculadoraCientifica(Calculadora):
    def realizar_operacion(self, tipo, n1, n2=None):
        alias = {"sqrt": "raiz", "ln": "logaritmo", "log10": "logaritmo"}
        tipo = alias.get(tipo.lower().strip(), tipo)
        return super().realizar_operacion(tipo, n1, n2)


# ================
#   MENÚ (VISTA)
# ================
def leer_float(mensaje):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Entrada no válida. Ingrese un número.")

def pausar():
    input("\nPresione ENTER para continuar...")

def mostrar_historial(calc):
    print("\n HISTORIAL DE OPERACIONES")
    historial = calc.get_historial()
    if not historial:
        print("No hay operaciones registradas.")
    else:
        for i, op in enumerate(historial, start=1):
            print(f"{i}. {op}")
    pausar()

def menu():
    calc = CalculadoraCientifica()
    opciones = {
        "1": "Suma",
        "2": "Resta",
        "3": "Multiplicación",
        "4": "División",
        "5": "Potencia",
        "6": "Raíz",
        "7": "Logaritmo",
        "8": "Ver Historial",
        "9": "Salir"
    }

    while True:
        print("\n============================")
        print("     CALCULADORA POO")
        print("============================")
        for k in sorted(opciones.keys(), key=int):
            print(f"{k}. {opciones[k]}")
        eleccion = input("Seleccione una opción: ").strip()

        try:
            if eleccion == "1":
                n1 = leer_float("Ingrese el primer número: ")
                n2 = leer_float("Ingrese el segundo número: ")
                print(f"Resultado: {calc.realizar_operacion('suma', n1, n2)}")
                pausar()
            elif eleccion == "2":
                n1 = leer_float("Ingrese el minuendo: ")
                n2 = leer_float("Ingrese el sustraendo: ")
                print(f"Resultado: {calc.realizar_operacion('resta', n1, n2)}")
                pausar()
            elif eleccion == "3":
                n1 = leer_float("Ingrese el primer factor: ")
                n2 = leer_float("Ingrese el segundo factor: ")
                print(f"Resultado: {calc.realizar_operacion('multiplicacion', n1, n2)}")
                pausar()
            elif eleccion == "4":
                n1 = leer_float("Ingrese el dividendo: ")
                n2 = leer_float("Ingrese el divisor: ")
                print(f"Resultado: {calc.realizar_operacion('division', n1, n2)}")
                pausar()
            elif eleccion == "5":
                n1 = leer_float("Ingrese la base: ")
                n2 = leer_float("Ingrese el exponente: ")
                print(f"Resultado: {calc.realizar_operacion('potencia', n1, n2)}")
                pausar()
            elif eleccion == "6":
                n1 = leer_float("Ingrese el número: ")
                print(f"Resultado: {calc.realizar_operacion('raiz', n1)}")
                pausar()
            elif eleccion == "7":
                n1 = leer_float("Ingrese el número: ")
                if input("¿Desea especificar base? (s/N): ").strip().lower() == "s":
                    base = leer_float("Base: ")
                    print(f"Resultado: {calc.realizar_operacion('logaritmo', n1, base)}")
                else:
                    print(f"Resultado: {calc.realizar_operacion('logaritmo', n1)}")
                pausar()
            elif eleccion == "8":
                mostrar_historial(calc)
            elif eleccion == "9":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except Exception as e:
            print(f" Error: {e}")
            pausar()


if __name__ == "__main__":
    menu()
