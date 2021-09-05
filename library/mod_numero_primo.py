 #Punto 3
def punto3():
    numero = int(input("Escriba cualquier numero para determinar si es numero perfecto: "));

    i = 1
    comprobar = 0;
    while(i < numero):
        if(numero%i == 0):
            comprobar = comprobar + i
        i = i +1

    if(comprobar == numero):
        return print("Este numero es perfecto!!")
    else:
        return print("Este numero no es perfecto!!")
