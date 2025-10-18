#while  estrucutra repetiva 
"""
x = 1

while x <= 11: 
    print (x)
    #x += 1
    x = x + 1



"""


frase =" Lo que escribas lo repito"
frase += "\nIntrodute el comando salir para finalizar. \n"

mensaje = "" 

while mensaje != "salir":
    mensaje = input(frase)
    print (mensaje)

# fuera del bucle
print (" Se ha salido del bucle")

""""
x = 1

while print (x) <= 10:
    print (x)
    if x == 6:
        break # break para salir del bucle - continue continua 
    x += 1
    
else:
     print (" Termino el bucle ") 

"""