class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 20)
print(p.edad)   # Acceso directo
p.edad = -5     # ❌ Se permite algo incorrecto
print(p.edad)


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre      # atributo privado
        self.__edad = edad          # atributo privado

    # Getter
    def get_edad(self):
        return self.__edad

    # Setter
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

p = Persona("Ana", 20)
print(p.get_edad())   # ✅ Obtener valor
p.set_edad(25)        # ✅ Modificar valor
p.set_edad(-5)        # ❌ Rechazado


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def edad(self):              # Getter
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):  # Setter
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

p = Persona("Ana", 20)
print(p.edad)     # ✅ parece acceso directo, pero usa getter
p.edad = 30       # ✅ parece asignación directa, pero usa setter
p.edad = -10      # ❌ controlado


"""Resumen para enseñar

Getter → Leer un atributo protegido.
Setter → Modificar un atributo de forma controlada.
Se usan para encapsular y validar datos.
En Python se pueden usar métodos tradicionales (get_edad, set_edad) 
o la forma más limpia con @property."""