# Parte 2:
# Nuevos req:
# -Validar que los nombres ingresados sean solo letras
# -Agregar al menu la funcion de eliminar un alumno, solicitando su nombre

alumnos = []

import re
def es_nombre_valido(nombre):
    return bool(re.match("^[a-zA-Z]+$", nombre))

while True:
    print("Menu:")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Eliminar alumno")
    print("4. Cerrar")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ")
        if es_nombre_valido(nombre):
            alumnos.append(nombre)
            print("Alumno agregado.")
        else:
            print("Nombre invalido. Ingrese solo letras.")
    elif opcion == "2":
        print("Lista de alumnos:")
        for alumno in alumnos:
            print(alumno)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        if nombre in alumnos:
            alumnos.remove(nombre)
            print("Alumno eliminado.")
        else:
            print("Alumno no encontrado.")
    elif opcion == "4":
        print("Cerrando el programa.")
        break
    else:
        print("Opcion invalida. Intente de nuevo.")
