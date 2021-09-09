#OPCION 4 YILBERTH ANDRES
def factorial(num):
    i = 0
    valor = 1
    for i in range(1, num +1):
        valor = valor * i
    return valor



def punto4():

    print("Para calcular la funcion exponencial se tomara n = 50 como constante")
    numero = int(input("Escriba cualquier numero para darle valor a x: "))

    valor = 0;
    for i in range(1,51):

        if(i == 1):
            contenedor = 1 + numero
        if(i > 1):
            contenedor = contenedor + ((numero**i)/(factorial(i)))
            
    
    return print("Respuesta: ", contenedor)
