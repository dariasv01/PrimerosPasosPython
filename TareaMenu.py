import re


agenda = {}

def mostrarAgenda():
    print("---Agenda---")
    for k, v in agenda.items():
        print(f"Contacto {k} - Teléfono {v}\n")

def addTelephone(nombre):
    tlfn = input("Introduce el teléfono XXXXXXXXX: ")
    if (re.findall(r"[\d]{9}", tlfn)):
        agenda[nombre] = tlfn
    else:
        print(f"Número incorrecto")
        command = input("1 Para volver al menú\nPara volver a añadir un número pulse otro\n")
        match command:
            case '1':
                agendaMostrar()
            case other:
                addTelephone(nombre)
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
    addTelephone(nombre)


def agendaMostrar():
    command = input("1 para mostrar agenda\n2 Para añadir contacto\n3 Para eliminar contacto\n0 Para salir\n")

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
        case '0':
            exit()
        case other:
             agendaMostrar()

agendaMostrar()