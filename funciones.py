# para definir una funcion utilizamos def, son reutilizables, 
# pueden llamarse las veces que las necesitemos 

def nombre_funcion ():
    print (4+3)


nombre_funcion ()
nombre_funcion ()
nombre_funcion ()

# Funciones con parametros y argumentos 

def  informacion (mensaje):
    print (mensaje)
    print (f"El mensaje es : {mensaje}")


informacion ("hola mundo")
informacion ("Trayecto de formacion Profesional")
informacion ("Monteros")


#Ejercicio: agregar un nuevo parametros a la funcion y al print. Al llamar a la funcion cargar el nuevo argumento

def saludar (nombre):
    print (f"hola, {nombre}")

saludar ("juan")

def saludar1 (nombre, edad):
   print (f"hola, {nombre}. Tienes {edad} años.")
   
saludar1 ("Juan", 35) 

# Funciones que nos devuelven un valor y despues se puede procesar esa  informacion 

def retornar (apellido):
    return apellido

empleado = retornar ("PEREz")



print ("hola",empleado.lower())