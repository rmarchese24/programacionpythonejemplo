# Lista es una coleccion de datos, mutables, podemos definir listas anidadas.
lenguajes = ["Python", "Javascript", "PHP", "C++", "Java"]
print (lenguajes)

# los arreglos (list) comoienzan en posicion 0
print (lenguajes[0]) # Python 
print (lenguajes[2]) # PHP

# Ordenar los elementos 
lenguajes.sort()
print (lenguajes)

# Acceder a un elemento de la lista  e insertar en cadena de caracter fstring
aprendiendo = f"Estoy aprendiendo {lenguajes[4]}"
print (aprendiendo)

# Modificar los valores del arreglo
lenguajes [1] ="C"
print (lenguajes) 

# Agregar elementos append
lenguajes.append ("Ruby")
lenguajes.append ("Pascal")
lenguajes.append ("Delphi")
print (lenguajes)

# Eliminar elementos del
del lenguajes [3]
print (lenguajes)

# Agregar elementos en una posicion indicada insert
lenguajes.insert(2, "HTML")
print (lenguajes)
# Eliminar la ultima posicion  pop
lenguajes.pop()
print (lenguajes)
lenguajes.pop(1)
print (lenguajes)

# Elimina por el contenido del arreglo  remove 
lenguajes.remove("C++")
print (lenguajes)