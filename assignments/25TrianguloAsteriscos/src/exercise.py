
def main():
    #Escribe tu código debajo de esta línea
    def trian(h):
        for i in range (h+1):
            e= h-i# los espacios 
            print(' '*e+'*'*i)
    
    h= int(input('Dame la altura de el trianlgulo:'))
    trian(h)
    
if __name__=='__main__':
    main()
