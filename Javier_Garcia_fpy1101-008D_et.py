import csv
import os
import random
import math
os.system
empleados = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"] 
sueldos={}
sueldo= {}
#sueldo aleatorio
def asignarSueldosAleatorios():
    for empleado in empleados:
        sueldos[empleado]= random.randint(300000,2500000)

#clasificacion
def clasificarSueldos():
    print("*****Clasificar Sueldos*****")
    menosDe800k={}
    entre800k_y_2m={}
    masDe2M = {}
    for empleado,sueldo in sueldos.items():
        if sueldo<800000:
            menosDe800k[empleado]=sueldo
        elif 800000<=sueldo<=2000000:
            entre800k_y_2m=sueldo
        else:
            masDe2M[empleado] =sueldo
    print("Sueldos menores a 800.000 Total:{}".format(len(menosDe800k)))
    for empleado,sueldo in menosDe800k.items():
        print(f"{empleado}:${sueldo}")
    print("Sueldos Entre 800.000 y 2.000.000n Total:{}".format(len(entre800k_y_2m)))
    for empleado,sueldo in entre800k_y_2m.items():
        print(f"{empleado}:${sueldo}")
    print("Sueldos superiores a 2.000.000 Total:{}".format(len(masDe2M)))
    for empleado,sueldo in masDe2M.items():
        print(f"{empleado}:${sueldo}")

#estadisticas
def verEstadisticas():
    sueldoMasAlto= max(sueldos.values())
    sueldoMasBajo= min(sueldos.values())
    promedioSueldo= sum(sueldos.values())/len(sueldos)
    mediaGeometrica= math.exp(sum(math.log(sueldo)))
    for sueldo in sueldos.values()/len(sueldos):
        print(f"Sueldo mas alto:${sueldoMasAlto}")
        print(f"Sueldo mas bajo:${sueldoMasBajo}")
        print(f"promedio de sueldo:${promedioSueldo:2f}")
        print(f"La media geometrica de sueldos:${mediaGeometrica}")

def reporteDeSueldo():
    reporte=[]
    for empleado,sueldos in sueldos.items():
        descuentoSalud = sueldo * 0.07
        descuentoAfp = sueldo *  0.12
        sueldoLiquido = sueldo - descuentoSalud - descuentoAfp
        reporte.append([empleado,sueldo,descuentoSalud,descuentoAfp,sueldoLiquido])
        with open('reporte_Sueldos.csv','w',newline='')as file:
            writer = csv.writer(file)
            writer.writerow(["Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
            writer.writerows(reporte)
        for  fila in reporte:
            print(f"{fila[0]}-sueldo base:${fila[1]},Desceunto Salud:${fila[3]:2f},Sueldo liquido:${fila[4]:2f}")

def salir():
    print("Sliendo del programa.....")
    print("Desarrollado por javier Garcia....21.655.097-8")

def menu():
            while True:
                print("\nMenu")

                print("(1)Asignar Sueldos Aleatorios")
                print("(2)Clasificar sueldos")
                print("(3)Ver Estadisticas.")
                print("(4)Reporte de sueldos")
                print("(5)Salir del programa")
                opciones = int(input("Ingrese una opcion:"))

                if opciones==1:
                    asignarSueldosAleatorios()

                elif opciones==2:
                    clasificarSueldos()

                elif opciones==3:
                    verEstadisticas()

                elif opciones==4:
                    reporteDeSueldo()

                elif opciones==5:
                    salir()
                    break
                else:
                    print("Ingrese una opcion valida porfavor")

menu()