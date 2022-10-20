""""
Funcion contraseña es segura
"""

import re

def passwordSave(passwordTest):

    if(re.findall(r"^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$", passwordTest)):
        return True
    else:
        return False

passwordPrueba = input("Introduce contraseña: ")

if passwordSave(passwordPrueba):
    print("Contraseña segura")
else:
    print("Contraseña insegura")