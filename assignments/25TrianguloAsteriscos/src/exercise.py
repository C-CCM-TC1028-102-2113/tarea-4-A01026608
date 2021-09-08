
def main():
    #Escribe tu código debajo de esta línea
   def trian(h):
        j=1
        for i in range (h,0,-1):
            espacios= " "*i
            asteriscos= '*' *j
            j= j+1
            print(espacios, asteriscos)

    h= int(input('Dame un número:'))
    trian(h)    
if __name__=='__main__':
    main()
