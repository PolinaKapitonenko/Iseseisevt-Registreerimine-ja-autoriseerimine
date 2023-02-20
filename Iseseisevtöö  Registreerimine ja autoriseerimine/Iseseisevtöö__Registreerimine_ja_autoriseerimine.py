from math import*
from random import*
from module1  import*


log=["User1", "User2"]
parool=["s1mple", "juppi"]
while True:
    print(log)
    print(parool)
    a=str(input("Kas soovite sisse logida? ")) #yas/no
    if a=="yas":
        print("Logi sisse")
        print("Sisestage oma sisselogimine ja parool")
        log=input("Logi sisse: ")
        pass_=input("Parool: ")
        if log in log and pass_ in parool:
            print("Olete edukalt sisse loginud ")

        elif print("Vale sisselogimine või parool"):
            print("")


    elif a=="no":
         b=str(input("Kas soovite registreeruda? "))
         b=="yas"
         print("registreerimine")
         log,parool=registreerimine(log,parool)
    else:
         b=="no"
         c=str(input("lõpeta töö? ")) #ainult yas
         if c=="yas":
            print("Lõpp") 
            break



         