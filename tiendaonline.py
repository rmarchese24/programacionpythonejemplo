from abc import ABC, abstractmethod
from datetime import datetime

# ==========================
# Clase abstracta Producto
# ==========================
class Producto(ABC):
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre          # Encapsulación
        self._precio = precio
        self._stock = stock

    @abstractmethod
    def mostrarInfo(self):
        pass

    def descontarStock(self, cantidad):
        if cantidad <= self._stock:
            self._stock -= cantidad
            return True
        else:
            print(f"No hay suficiente stock de {self._nombre}.")
            return False

    def getPrecio(self):
        return self._precio

    def getNombre(self):
        return self._nombre

    def getStock(self):
        return self._stock


# ==========================
# Subclases de Producto
# ==========================
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, marca, garantia):
        super().__init__(nombre, precio, stock)
        self._marca = marca
        self._garantia = garantia

    def mostrarInfo(self):
        return f"[Electrónico] {self._nombre} - ${self._precio} | Stock: {self._stock} | Marca: {self._marca} | Garantía: {self._garantia} meses"


class ProductoRopa(Producto):
    def __init__(self, nombre, precio, stock, talla, color):
        super().__init__(nombre, precio, stock)
        self._talla = talla
        self._color = color

    def mostrarInfo(self):
        return f"[Ropa] {self._nombre} - ${self._precio} | Stock: {self._stock} | Talla: {self._talla} | Color: {self._color}"


# ==========================
# Clase Carrito (Composición)
# ==========================
class Carrito:
    def __init__(self):
        self._items = []  # lista de tuplas (producto, cantidad)

    def agregarProducto(self, producto, cantidad):
        if producto.getStock() >= cantidad:
            self._items.append((producto, cantidad))
            print(f"Se agregó {cantidad} x {producto.getNombre()} al carrito.")
        else:
            print("No hay suficiente stock para agregar al carrito.")

    def quitarProducto(self, producto):
        self._items = [item for item in self._items if item[0] != producto]
        print(f"Producto {producto.getNombre()} eliminado del carrito.")

    def calcularTotal(self):
        return sum(producto.getPrecio() * cantidad for producto, cantidad in self._items)

    def getItems(self):
        return self._items

    def vaciar(self):
        self._items = []


# ==========================
# Clase Pedido (Asociación)
# ==========================
class Pedido:
    contador = 1

    def __init__(self, productos, total):
        self.numero_pedido = Pedido.contador
        Pedido.contador += 1
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.productos = productos
        self.total = total

    def mostrarResumen(self):
        print(f"\n--- Pedido N° {self.numero_pedido} ---")
        print(f"Fecha: {self.fecha}")
        for producto, cantidad in self.productos:
            print(f"{cantidad} x {producto.getNombre()} - ${producto.getPrecio()}")
        print(f"TOTAL: ${self.total}")
        print("---------------------------")


# ==========================
# Clase Cliente (Agregación)
# ==========================
class Cliente:
    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email
        self._carrito = Carrito()
        self._pedidos = []

    def getCarrito(self):
        return self._carrito

    def realizarCompra(self):
        if not self._carrito.getItems():
            print("El carrito está vacío, no se puede realizar la compra.")
            return

        # Descontar stock
        for producto, cantidad in self._carrito.getItems():
            producto.descontarStock(cantidad)

        # Crear pedido
        total = self._carrito.calcularTotal()
        pedido = Pedido(self._carrito.getItems(), total)
        self._pedidos.append(pedido)

        # Mostrar resumen
        pedido.mostrarResumen()

        # Vaciar carrito
        self._carrito.vaciar()

    def mostrarHistorial(self):
        print(f"\nHistorial de pedidos de {self._nombre}:")
        for pedido in self._pedidos:
            pedido.mostrarResumen()


# ==========================
# Ejemplo directo (sin if __main__)
# ==========================
# Crear productos
laptop = ProductoElectronico("Laptop", 1200, 5, "Dell", 24)
camiseta = ProductoRopa("Camiseta", 25, 10, "M", "Azul")

# Crear cliente
cliente1 = Cliente("Juan Perez", "juan@example.com")

# Cliente agrega productos
carrito = cliente1.getCarrito()
carrito.agregarProducto(laptop, 1)
carrito.agregarProducto(camiseta, 2)

# Cliente realiza compra
cliente1.realizarCompra()

# Ver historial
cliente1.mostrarHistorial()
