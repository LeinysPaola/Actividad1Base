from library.mod_numero_primo import *
from library.mod_funcion_exponencial import *
from library.mod_numero_perfecto import *
from library.mod_numero_par_o_impar import *

def opciones():
    op = 0
    
   
    while(op < 1 or op > 4):
        print("             ACTIVIDAD 1        ")
        print("")
        print("")
        print("1............Ver si un numero es par o impar.")
        print("2............Ver si un numero si es primo o no.")
        print("3............Ver si un numero si un numero es perfecto.")
        print("4............Calcule una funcion exponencial.")
        print("")
        op = int(input("Que opcion elijes: "))
        print("")

        if(op < 1 or op > 4):
            print("Por favor elija una opcion entre 1 y 4")
    if (op == 1):
        punto1()   
    if (op == 2):
        punto2()
    if(op == 3):
        punto3()
    if(op == 4):
        punto4()

