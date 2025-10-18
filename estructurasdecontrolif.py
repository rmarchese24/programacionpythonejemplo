# Condicional If  . selectiva 
# Operadores de comparacion 
# > mayor
# < menor
# >= mayor igual
#< = menor igual
# == igual a
precio = 500
print(precio)
precio = int(input("Ingrese un numero "))
print(precio)
if precio > 600:
    print ("Tiene descuento")
else:
    print (" No tiene descuento")


"""
if precio == 500:
    print ("Tiene descuento")
else:
    print (" No tiene descuento")

# if elif else

edad = int (input (" Ingresa tu edad:   "))
if 0 < edad < 16:
    print (" No vota")
elif edad <= 0:
    print (" Edad no validad")
else:
    print ( " Puede votar")
    
print (" Fin de la evaluacion de edad ")

# Operadores logicos  and y or  (y - o)

usuario_registrado = False
usuario_administrador = False

if usuario_registrado and usuario_administrador:
    print ("Verdadero")
elif usuario_registrado:
    print ("Usuario verdadero")
else:
    print("debes ingresar siendo Verdadero")

"""