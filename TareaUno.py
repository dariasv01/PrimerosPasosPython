# numberFac = int(input("Introduce un numero "))

# for i in range(2,(numberFac+1)):
#     res = res + multi()

"""
res = 1

def multi(numberOne, numberTwo):
    return numberOne*numberTwo


def factorial(num):
    if(num>0):
        return num*factorial(num-1)
    else:
        return 1


print(f"Resultado {factorial(0)}")
print(f"Resultado {factorial(5)}")
print(f"Resultado {factorial(12)}")
"""
import random

# Ejercicio dos
"""

l =("David",1,2,5,2,"David","Arias",3,5)

print(l)

l=list(set(l))

print(l)
"""

# Ejercicio tres
"""
l =("David",1,2,5,2,"David","Arias",3,5)
l2 =("Vizano",1,6,5,8,"David","Arias",3,9)
print(l)

lr=list(set(l)|set(l2))

print(lr)

lr = set(l)-set(l2)
print(lr)

#Ejercicio 5

frase = input("Introduce una frase:")

fraseSinEspacio =[]

for i in frase:
    if i !=" ":
        fraseSinEspacio.append(i)

print(f"La longitud de la frase resultante es: {len(fraseSinEspacio)}\nY de la original: {len(frase)}")

frase=frase.replace(" ","")

print(f"La longitud de la frase resultante es: {len(frase)}")




# Ejercicio 6

frase = list(input("Introduce una frase:"))
fraseRes = []
contador = len(frase)
for i in range(0, contador):
    # print(f"Longitud {len(frase)}")
    index = random.randint(0, len(frase) - 1)
    fraseRes.append(frase[index])
    # print(index)
    frase.pop(index)

print(f"Resultado {fraseRes}")

"""
#Ejercicio 7

