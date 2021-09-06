def main():
    #escribe tu código abajo de esta línea
    num= int(input())
    for numero in range (num):
        if numero%2==0:
            print('#')
        else:
            print('%')
if __name__=='__main__':   
    main()
