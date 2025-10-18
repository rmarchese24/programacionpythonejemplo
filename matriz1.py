matriz = [ [1,2,3],
[2,5,1],
[6,5,1]    ]

suma=0
i=0
while(i<len(matriz)):
    fila=matriz[i]
    j=0
    while(j<=len(fila)):
        if i==j:
            suma+=fila[j]
        j+=1
    i+=1
    
        
print(f"La suma de los elementos de la diagonal es: {suma}")
