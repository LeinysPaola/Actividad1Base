from mod_numero_perfecto import *

def opciones():
    op = 0
    while(op < 1 or op > 4):

        op = int(input("Que opcion elijes: "))

        if(op < 1 or op > 4):
            print("Por favor elija una opcion entre 1 y 4")
        
 
    if(op == 3):
        punto3()