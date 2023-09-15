from time import sleep


a=int(input("Digite um tempo em segundos: "))

while a>=1 :
    print(a)
    sleep(1)
    a=a-1
    if a==0 :
        print("Seu tempo acabou")
