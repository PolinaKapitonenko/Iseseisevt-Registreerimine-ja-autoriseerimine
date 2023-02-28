from random import*
import string
from random import *
import string
def salasona(k: int)->bool:
    """
    Määrme salasõna..
    :parem int k:Järjend salasõna numbridest
    :rtype: bool
    """
    saladus=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus

def registreerimine(log:list, parool:str)->bool:
    """
    Määrme reg..
    :parem log list, pas str:Järjend salasõna numbridest
    :rtype: bool
    """
    n=input("Kirjuta oma nimi: ")
    tehe=int(input("2-Määrake oma parool, 1-Looge see juhuslikult\n "))

    if tehe==1:
        salasona=salasona(12)
        log.append(n)
        parool.append(salasona)
 

    elif tehe==2:
       parool=input("Kirjutage oma parool: ")
       if any(c.islower() for c in parool) and any(c.isupper() for c in parool) and any(c.isdigit() for c in parool) and any(c in '.,:;!_*-+()/#¤%&' for c in parool):
            print("Olete loonud parooli")
            log.append(n)
            parool.append(str(salasona))
       else:
            print("Viga!!!")
        
       
    return log,parool


def muuda_nimi(log: list, parool: list) -> None:
    """
    Muutke olemasoleva kasutaja kasutajanime
    """
    n = input("Sisestage kasutajanimi, mille nime soovite muuta: ")
    if n in log:
        new_n = input("Sisestage uus kasutajanimi: ")
        index = log.index(n)
        log[index] = new_n
        print(f"Kasutajanimi on muudetud. Uus nimi on {new_n}.")
    else:
        print("Viga!!! Kasutajanime ei leitud.")

def muuda_parool(log: list, parool: list) -> None:
    """
    Muutke olemasoleva kasutaja parooli
    """
    n = input("Sisestage kasutajanimi, mille parooli soovite muuta: ")
    if n in log:
        index = log.index(n)
        new_password = input("Sisestage uus parool: ")
        parool[index] = new_password
        print("Parool on muudetud.")
    else:
        print("Viga!!! Kasutajanime ei leitud.")

def unustanud_parool(log: list, parool: list) -> None:
    """
    Lähtestab olemasoleva kasutaja parooli.
    """
    kasutaja = input("Sisestage oma kasutajanimi: ")
    if kasutaja in log:
        index = log.index(kasutaja)
        uus_parool = input("Sisestage uus parool: ")
        parool[index] = uus_parool
        print("Teie parool on edukalt lähtestatud!")
    else:
        print("Sellist kasutajanime pole olemas.")

def lopeta() -> None:
    """
    Lõpetab programmi.
    """
    print("Lõpetamine")
    


        
   