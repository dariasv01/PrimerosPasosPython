import re

agenda = {}

def mostrarAgenda():
    for k, v in agenda.items():
        print(f"{k}:{v}\n")

def borrarContacto():
    nombre = input("Introduce el nombre del contacto: ")
    if(agenda.__contains__(nombre)):
        agenda.pop(nombre)
    else:
        selector = input(f"El nombre {nombre} no existe\nPulse 1 para eliminar otro contacto o pulse cualquier letra para salir")
        if(selector=="1"):
            borrarContacto()
        else:
            mostrarAgenda()

def anadirContacto():
    nombre = input("Introduce el nombre del contacto: ")

    tlfn = input("Introduce el teléfono XXX-XXX-XXX: ")
    if(re.findall(r"[\d]{3}-[\d]{3}-[\d]{3}", tlfn)):
       agenda[nombre] = tlfn
    else:
       print(f"Número incorrecto")
       anadirContacto()

def agendaMostrar():
    command = input("1 para mostrar agenda\n2 Para añadir contacto\n3 Para eliminar contacto\n")

    match command:
        case '3':
            borrarContacto()
            agendaMostrar()
        case '2':
            anadirContacto()
            agendaMostrar()
        case '1':
            mostrarAgenda()
            agendaMostrar()
        case other:
             agendaMostrar()

agendaMostrar()