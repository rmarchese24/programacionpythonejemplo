class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    # Getter
    def get_saldo(self):
        return self.__saldo

    # Setter
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("❌ Error: El saldo no puede ser negativo.")

    # Método para depositar
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"✅ Depósito de {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("❌ Error: El depósito debe ser mayor a 0.")

    # Método para retirar
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"✅ Retiro de {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("❌ Error: Fondos insuficientes o cantidad inválida.")


# 🔹 Ejemplo de uso
cuenta = CuentaBancaria(1000)
print(cuenta.get_saldo())  # 1000
cuenta.set_saldo(500)      # Cambia saldo
print(cuenta.get_saldo())  # 500
cuenta.depositar(200)      # Saldo: 700
cuenta.retirar(300)        # Saldo: 400
cuenta.set_saldo(-50)      # ❌ No permite
