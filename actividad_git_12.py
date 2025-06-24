# Parte I:
# Caso:
# Crear un programa python con un menu, con tres opciones. 
# 1 Agregar alumnos a una lista de alumnos, 
# 2. mostrar todos los alumnos, 
# 3. cerrar. El programa debe pedir el nombre del alumno.

alumnos = []

while True:
    print("Menu:")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Cerrar")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ")
        alumnos.append(nombre)
        print("Alumno agregado.")
    elif opcion == "2":
        print("Lista de alumnos:")
        for alumno in alumnos:
            print(alumno)
    elif opcion == "3":
        print("Cerrando el programa.")
        break
    else:
        print("Opcion invalida. Intente de nuevo.")

