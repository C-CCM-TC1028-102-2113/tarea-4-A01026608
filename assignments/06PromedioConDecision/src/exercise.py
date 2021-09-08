def main():
    #escribe tu código abajo de esta línea
    contador= 0
    suma= 0
    numero=1
    while True:
        numero= float(input())

        if numero<0:
            break
        suma= suma+numero
        contador= contador+1
        promedio= suma/contador
    print( promedio)

