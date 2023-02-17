from math import*
from random import*
from module1  import*


logt=["User1", "User2"]
pas=["s1mple", "juppi"]
while True:
    print(logt)
    print(pas)
    a=str(input("Kas soovite sisse logida? ")) #yas/no
    if a=="yas":
        print("Logi sisse")
        print("Sisestage oma sisselogimine ja parool")
        logi=input("Logi sisse: ")
        pass_=input("Parool: ")
        if logi in logt and pass_ in pas:
            print("Olete edukalt sisse loginud ")

        elif print("Vale sisselogimine või parool"):
            print("")


    elif a=="no":
         b=str(input("Kas soovite registreeruda? "))
         b=="yas"
         print("registreerimine")
         logt,pas=registreerimine(logt,pas)
    else:
         b=="no"
         c=str(input("lõpeta töö? ")) #ainult yas
         if c=="yas":
            print("Lõpp") 
            break
         