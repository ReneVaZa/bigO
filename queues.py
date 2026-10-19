from collections import deque
import time
cola=deque()

cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")

atendido=cola.popleft()
print("Atendido",atendido)
print("cola restante: ",cola)

cola_reproduccion=deque()

cola_reproduccion.append("1.antologia")
cola_reproduccion.append("2.historia de amor")
cola_reproduccion.append("3.historia entre tus dedos")

print("canciones en espera:")
for cancion in cola_reproduccion:
    print(" _",cancion)
    print("iniciando reproduccion")

while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"sonando ahora{cancion_actual}")
    time.sleep(1)
    print(f"finalizo:{cancion_actual}")

    print(f"Quedan{len(cola_reproduccion)} canciones en la cola")
    print("la cola de reproduccion ha terminado")

