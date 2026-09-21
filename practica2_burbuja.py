lista = [10,6,7,8,8,6,9,10,10,8,5,2,7,4,9]
n = len(lista)
swapped = True
while swapped:
    swapped= False 
    for i in range(n-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            swapped = True
print("Lista ascendente:",lista)

print()

swapped = True
while swapped:
    swapped= False 
    for i in range(n-1):
        if lista[i]<lista[i+1]:
            lista[i], lista[i+1]=lista[i+1],lista[i]
            swapped = True
print("Lista decendente:",lista)  
