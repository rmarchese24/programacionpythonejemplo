# Calcular el factorial de un numero ingresado por el usuario, el numero debe ser posivo

""" comentarios de varias lineas
lineas
lineas


num = int ( input("Ingrese un número entero positivo:     "))

# bucle para validar si el numero es positivo
while num < 0:
    print (" debe ingresar un numero positivo")
    num = int ( input("Ingrese nuevamente un número entero positivo:     "))

factorial = 1
i = 1

# calculo de factorial

while i <= num: 
    factorial *= i
    #factorial = factorial * i  es igual a la anterior linea
    i += 1
    
print (f" El factorial del numero {num} es igual al {factorial}")

"""
num = int ( input("Ingrese un número entero positivo:     "))

# bucle para validar si el numero es positivo
while num < 0:
    print (" debe ingresar un numero positivo")
    num = int ( input("Ingrese nuevamente un número entero positivo: " ))

factorial1 = 1

# calculo de factorial

for i in range (1,(num+1)):
    factorial1 *= i
   
    #factorial = factorial * i  es igual a la anterior linea
       
print (f" El factorial del numero {num} es igual al {factorial1}")