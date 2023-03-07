from math import*
from random import*
from module1  import*


log=["User1", "User2"]
parool=["s1mple", "juppi"]
while True:
    print(log)
    print(parool)
    a=str(input("Kas soovite sisse logida? ")) #yas/no
    if a=="jah":
        print("Logi sisse")
        print("Sisestage oma sisselogimine ja parool")
        log=input("Logi sisse: ")
        pass_=input("Parool: ")
        if log in log and pass_ in parool:
            print("Olete edukalt sisse loginud ")

        else:
           print("Vale sisselogimine või parool")
           print("")
           break

    elif a=="ei":
         b=str(input("Kas soovite registreeruda? "))
         b=="jah"
         print("registreerimine")
         log,parool=registreerimine(log,parool)
    else:
         b=="ei"
         c=str(input("lõpeta töö? ")) #ainult yas
         if c=="jah":
            print("Lõpp") 
            break


while True:
    print(log)
    print(parool)
    valik = input("Kas soovite sisse logida? (jah/ei): ")
    if valik == "jah":
        print("Logi sisse")
        kasutaja = input("Sisestage oma sisselogimine: ")
        parool_sisestatud = input("Sisestage oma parool: ")
        if kasutaja in log and parool_sisestatud == parool[log.index(kasutaja)]:
            print("Olete edukalt sisse loginud!")
        else:
            print("Vale sisselogimine või parool")
            break
         