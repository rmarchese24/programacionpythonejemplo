dict1 = {'one': 1, 'two': 2, 'three': 3}
print(dict1)
dict1.clear()
print(dict1)

dict1 = {'one': 1, 'two': 2, 'three': 3}
dict2 = dict1.copy()
print(dict1)
print(dict2)

dict1 = {'one': 1, 'two': 2, 'three': 3}
dict2 = {'four':4,'five':5}
dict1.update(dict2)
print(dict1)
print(dict2)

for clave in dict1.keys():
    print(clave)

for valor in dict1.values():
    print(valor) 

for clave,valor in dict1.items():
    print(clave,"->",valor)
