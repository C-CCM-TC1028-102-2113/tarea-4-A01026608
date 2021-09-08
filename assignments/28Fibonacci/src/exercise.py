
def main():
    #escribe tu código abajo de esta línea
    x= 0
    y=1
    indice=1
    n= int(input('Enter a number:'))

    if n==0:
        print(0)
    if n==1:
        print(1)
    while indice<n:
        indice=indice+1 
        z= x+y
        if n==indice:
            print(z)
        x=y
        y=z
        
if __name__=='__main__':
    main()
