#OPCION 4

def factorial(num):
    i = 0
    valor = 0
    for i in range(1, num +1):
        valor = valor * i



def punto4():

    print("Para calcular la funcion exponencial se tomara n = 50 como constante")
    numero = int(input("Escriba cualquier numero para darle valor a x"))

    i = 1
    valor = 0;
    for i in range(1,3):

        if(i == 1):
            contenedor = 1 + numero
        if(i > 1):
            factorial(contenedor)
    
    return contenedor

        

        
