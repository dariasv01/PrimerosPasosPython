"""
Esto es un
comentario en bloque
"""
from nis import match

# Comentario en linea

print("Hola Mundo")

nombre = "Me llamo Carlos"

print(dir(nombre))

print(nombre.rsplit("a",1))

print("---------")

edad = int(input("Introduc tu edad "))

#print("Tu edad es",edad)

# print(f"Tu edad es {edad}")
# if(edad<18):
#     print("Hola bebe")
# elif(edad>33):
#     print("Eres un yayo")
# else:
#     print("Eres joven")

for i in range (1,10,2):
    print(i)

def annio(edad):
    print(f"Tu edad es {edad}")
    if(edad<18):
        print("Hola bebe")
    elif(edad>33):
        print("Eres un yayo")
    else:
        print("Eres joven")

annio(edad)

