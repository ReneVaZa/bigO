import numpy as np

matrizA=np.array([[10, 15],
                   [20, 5]])
matrizB=np.array([[5, 12],
                  [15, 8]])

totalVentas=matrizA+matrizB
precio= 50
ingresoTotal=totalVentas*precio

print("Matriz de Ventas Totales (Unidades):")
print(totalVentas)
print("Matriz de Ingreso Total(Pesos)")
print(ingresoTotal)

totalVentasNat=[]
for i in range(len(matrizA)):
    fila=[]
    for j in range(len(matrizA[i])):
        sumaElementos=matrizA[i][j]+matrizB[i][j]
        fila.append(sumaElementos)
    totalVentasNat.append(fila)


ingresoTotalNat=[]
for i in range(len(totalVentasNat[i])):
    fila=[]
    for j in range(len(totalVentasNat[i])):
        multiplicacion=totalVentasNat[i][j]*precio
        fila.append(multiplicacion)
    ingresoTotalNat.append(fila)


print("Matriz de Ventas Totales (Unidades):")
for fila in totalVentasNat:
    print(fila)
print("Matriz de Ingreso Total(Pesos)")
for fila in ingresoTotalNat:
    print(fila)    
    
