import os
import time

inicio = time.time()

for i in range(5):
    print(i)

fin = time.time()
tiempoFinal = fin - inicio

print(f"""Tiempo de ejecución: {tiempoFinal}""")

time.sleep(5)

os.system("cls")

contador = 0

while contador <= 10:
    print(contador)
    contador += 1

fin = time.time()
tiempoFinal = fin - inicio

print(f"""Tiempo de ejecución: {tiempoFinal}""")


