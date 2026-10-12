lista = [15,3,8,1,22,9]
n = len(lista)
swapped = True
print("lista original: ",lista)
#Algoritmo de burbuja
while swapped:
    swapped= False 
    for i in range(n-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            swapped = True
print("Lista burbuja: ",lista)

#Algoritmo de seleccion
for i in range(n):
    menor = i
    for j in range(i + 1, n):
        if lista[j] < lista[menor]:
            menor = j
    lista[i], lista[menor] = lista[menor], lista[i]
print("Lista seleccion: ",lista)

#Algoritmo de insercion
for i in range(1, len(lista)):
    actual = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > actual:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = actual
print("Lista insercion: ",lista)

#Algoritmo QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)
resultado = quicksort(lista)

print("Lista QuickSort: ", resultado)



