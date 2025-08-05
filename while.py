import time
import os

palabra = input(str("ingrese una palabra: "))

while palabra.lower()== "s":
    palabra = input(str("ingrese una palabra: "))
print("fin del ciclo while")

time.sleep(3)
os.system("cls")

contador = 0

while True:
    if contador == 10:
        break
        print(contador)
        
    else:
        print("El contador no ha llegado a 10")
    contador += 1
    
    
