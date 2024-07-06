import random 
import globales
import json 

empleados = [
    "Luisa Morales",
    "Javier Torres",
    "Sofía Ramírez",
    "Martín Gutiérrez",
    "Valeria Castillo",
    "Diego Vargas",
    "Camila Ruiz",
    "Alejandro Medina",
    "Carolina Herrera",
    "Andrés Silva",
    "Paula Ortiz",
    "Gabriel Ramos"
]

def asignar_sueldo():

    todos_los_empleados= []
    for empleado in empleados:
        sueldo = random.randint(9000,15000) * 100
        salud = int(sueldo * 0.7)
        afp = int(salud * 0.12)
        sueldo_liquido = sueldo - afp -salud
        nuevo_sueldo = {
            "nombre": empleado,
            "salud": salud,
            "afp": afp,
            "sueldo_liquido": sueldo_liquido
        }
        todos_los_empleados.append(nuevo_sueldo)
    globales.guardar_archivo_json("sueldos.json",todos_los_empleados)

asignar_sueldo()