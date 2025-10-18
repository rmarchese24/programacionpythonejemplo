# Ej1: Definir una  vacía y luego solicitar al carga de 5 numeros 
# enteros por teclado y añadirlos a la lista. Imprimir la lista

"""lista = [] # defino una lista vacia
print ("Cargar 5 numeros enteros:")
num1 = int(input(" Ingrese el primer numero: "))
lista.append(num1) # agregamos el primer elemento 
print (lista)

for x in range (4):  # cargar los siguientes elementos
    x = int (input ("Ingrese un numero: "))
    lista.append (x) # agrega los elementos a la lista 
    print (lista) # salida de la lista parcial 
    

print(lista) # lista completa 

"""

# Ej2 Realizar la carga de valores enteros por teclado, almacenarlos en una 
# lista. Finalizar la carga de enteros al ingresar el numero cero. 
# Mostrar finalmente el tamaño de la lista con funcion len() y lista completa

# Ej3 Almacenar en una lista los sueldos   (valores float) de  5 operarios
# Imprimir la lista y el promedio de sueldo

sueldo = []

for z in range (5):
    z= float (input ("Ingresar el sueldo del operario: "))
    sueldo.append(z)

promedio = sum(sueldo)/len(sueldo) 
print(sueldo)
print (" El sueldo promedio es:  ", promedio)
