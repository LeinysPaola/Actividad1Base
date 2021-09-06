from library.mod_numero_primo import *
from library.mod_funcion_exponencial import *
from library.mod_numero_perfecto import *
from library.mod_numero_par_o_impar import *

def opciones():
    op = 0
    while(op < 1 or op > 4):

        op = int(input("Que opcion elijes: "))

        if(op < 1 or op > 4):
            print("Por favor elija una opcion entre 1 y 4")

    if(op == 1): 
        punto1()    
    if(op == 2):
        punto2()
    if(op == 3):
        punto3()
    if(op == 4):
        punto4()
