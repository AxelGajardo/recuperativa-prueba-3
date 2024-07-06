import globales
import os
import sueldos
import main
import estadisticas

def menu_estadisticas():
    while True:
        os.system("cls")
        print("=== Menu Estadisticas ===")
        print("1.- Generar Sueldo liquido mas alto")
        print("2.- Generar Sueldo liquido mas bajo ")
        print("3.- Generar Pormedio de sueldos liquidos")
        print("4.- Generar Media Geometrica de los sueldos liquidos")
        print("5.- Volver al menu anterior")

        opcion = globales.seleccionar_opcion(5)
        
        if opcion == 1:
            estadisticas.sueldo_liquido_mas_alto()
            input("Ingrese ENTER para continuar")
        elif opcion == 2:
            estadisticas.sueldo_liquido_mas_bajo()
            input("Ingrese ENTER para continuar")
        elif opcion == 3:
            estadisticas.promedio_sueldos()
            input("Ingrese ENTER para continuar")
        elif opcion == 4:
            estadisticas.media_geometrica_sueldo()
            input("Ingrese ENTER para continuar")
        elif opcion == 5:
            return 


def menu_principal():
    while True:
        os.system("cls")
        print("=== Menu Principal ===")
        print("1.- Asignar Sueldos Aleatorios")
        print("2.- Ver estadisticas ")
        print("3.- Salir del programa ")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("1.- Asignar Sueldos Aleatorios")
            sueldos.asignar_sueldo()
        elif opcion == 2:
            print("Ver estadisticas ")
            menu_estadisticas()
        elif opcion == 3:
            print("Adios")
            return False

if __name__ == "__main__":
    menu_principal()