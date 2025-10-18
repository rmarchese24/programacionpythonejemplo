from abc import ABC, abstractmethod
import os


os.system("cls")

# Clase abstracta y herencia:  Mascota  clase base y perro y gato subclase


class Corazon:
    def __init__(self, frecuencia_cardiaca = 90):
        self.frecuencia_cardiaca = frecuencia_cardiaca
       
    def latir (self):
        print (f" El corazon  tiene una frecuencia cardiaca {self.frecuencia_cardiaca}")
         
# clase abstracta   
class Mascota(ABC):
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.corazon = Corazon() # composicion
   
    def comer (self):
        print (f"{self.__nombre} esta comiendo")
   
    @abstractmethod
    def hacer_sonido (self):
        pass
   
    def mostrar_informacion (self):
        print(f"Nombre: {self.__nombre}, {self.__edad}")

    @abstractmethod
    def calcular_costo(self):
        pass

# clase subclase

class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
   
    def hacer_sonido(self):
        print (f"{self.__nombre} dice : Guau Guau!!")
   
    def calcular_costo(self):
        return 4000
       

class Gato(Mascota):
    def __init__(self, nombre, edad, color_pelo):
        super().__init__(nombre, edad)
        self.color_pelo = color_pelo
   
    def hacer_sonido(self):
        print (f"{self.__nombre} dice : Miuuuuuu!!")
    def calcular_costo(self):
        return 5000    
       
# Asociacion con clase Dueño

class Dueño:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
       
        self.mascotas = [] # lista de mascotas,  un dueño puede tener varias mascotas (asociacion  uno
   
    def registrar_mascota(self, mascota):
        if mascota not in self.mascotas:
            self.mascotas.append(mascota)
            print( f"la mascota Agregada {mascota}")
   
    def mostrar_mascota (self):
        print (f"Dueño : {self.nombre}, Tel : {self.telefono}")  
        for mas in self.mascotas:
            mas.mostrar_informacion()
            print(f"El costo {mas.calcular_costo()}")
           
# Agregacion Veterinaria y mascota
class Veterinaria:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.mascota_atendidas = [] # agregacion  - solo se agregaran las mascotas que se atiendan
           
    def atender_mascota (self, mascota):
        self.mascota_atendidas.append(mascota)  
        print(" Mascosta atendida agregada")  
           
    def mostrar_mascotas_atendidas (self):
        print (f"Veterinaria : {self.__nombre} atendio las siguientes mascotas")  
        for mas in self.mascota_atendidas:
            mas.mostrar_informacion()
            print(f"el costo es : {mas.calcular_costo()}")


#Programacion principal

# Crear el dueño
dueño1 = Dueño ("Juan Perez", 3863428108)
dueño2 = Dueño ("Pedro Diaz", 358719126)

# Crear las mascotas
firulai = Perro ("Firulais",7,"Callejero Aleman")
Michi = Gato ("Michi", 15, "Marron")
Lola = Gato ( " Lola ", 10, "Blanca")

# Asignar el dueño a la mascota

dueño1.registrar_mascota(firulai)
dueño2.registrar_mascota(Lola)
dueño1.registrar_mascota(Michi)

# Mostrar las cascotas de cada dueño
dueño1.mostrar_mascota()
dueño2.mostrar_mascota()

# Crear veterinaria

vet = Veterinaria ("San Roque")

# Atencion de la mascotas

vet.atender_mascota(firulai)
vet.atender_mascota(Michi)
vet.atender_mascota(Lola)

# Ver mascotas atendidas
vet.mostrar_mascotas_atendidas()

