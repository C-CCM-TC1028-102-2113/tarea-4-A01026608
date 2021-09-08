

def main():
    #Escribe tu código debajo de esta línea
    num= int(input('Inserte un número:'))
    a=1
    while num> a**2:
        a=a+1
        b=a**2
        if b>num:
            print(a)
            
if __name__=='__main__':
    main()
