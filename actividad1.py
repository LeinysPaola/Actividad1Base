<<<<<<< Updated upstream
from library.mod_opciones import *
        
   
def inicio():
    opciones()
 

if __name__== '__main__':
=======
from mod_numero_perfecto import *
from mod_funcion_exponencial import *
from mod_numero_primo import *
def opciones():
    op = 0
    while(op < 1 or op > 4):

        op = int(input("Que opcion elijes: "))

        if(op < 1 or op > 4):
            print("Por favor elija una opcion entre 1 y 4")
        
    if (op == 2):
        punto2()
    if(op == 3):
        punto3()
    if(op == 4):
        punto4()

def inicio():
    opciones()
 

if __name__== '__main__':
>>>>>>> Stashed changes
    inicio()