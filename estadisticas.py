import globales
import main
import math
import json

def sueldo_liquido_mas_alto():
    todos_los_sueldos = globales.leer_archivo_json("sueldos.json")

    sueldos_ordenados = sorted(todos_los_sueldos, key=lambda x: x["sueldo_liquido"], reverse= True)

    for sueldo in sueldos_ordenados[:1]:
        nombre = sueldo["nombre"]
        liquido_alto = sueldo["sueldo_liquido"]
    
    print(f"Nombre{nombre}    sueldo liquido{liquido_alto}")


def sueldo_liquido_mas_bajo():
    todos_los_sueldos = globales.leer_archivo_json("sueldos.json")

    sueldos_ordenados = sorted(todos_los_sueldos, key=lambda x: x["sueldo_liquido"], reverse= False)

    for sueldo in sueldos_ordenados[:1]:
        nombre = sueldo["nombre"]
        liquido_bajo = sueldo["sueldo_liquido"]
    
    print(f"Nombre{nombre}    sueldo liquido{liquido_bajo}")


def promedio_sueldos():
    todos_los_sueldos = globales.leer_archivo_json("sueldos.json")

    suma_sueldos = 0
    cantidad_sueldo = 0

    for sueldo in todos_los_sueldos:
        suma_sueldos += sueldo["sueldo_liquido"]
        cantidad_sueldo += 1

    promedio = int(suma_sueldos / cantidad_sueldo)
    print (f"El promedio de sueldo liquido es ${promedio}")


def media_geometrica_sueldo():
    todos_los_sueldos = globales.leer_archivo_json("sueldos.json")

    suma_sueldos = 0
    cantidad_sueldo = 0

    for sueldo in todos_los_sueldos:
        suma_sueldos += math.log(sueldo["sueldos_liquido"])
        cantidad_sueldo += 1
    
    geometrica = int(math.exp(suma_sueldos/cantidad_sueldo))
    print (f"La media gemotrica de los sueldos liquidos es ${geometrica}")
    