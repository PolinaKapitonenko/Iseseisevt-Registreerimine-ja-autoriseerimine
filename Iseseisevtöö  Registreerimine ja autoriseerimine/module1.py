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

def registreerimine(logt:list, pas:str)->bool:
    """
    Määrme reg..
    :parem logt list, pas str:Järjend salasõna numbridest
    :rtype: bool
    """
    n=input("Kirjuta oma nimi: ")
    tehe=int(input("2-Määrake oma parool, 1-Looge see juhuslikult\n "))

    if tehe==1:
        salasona=salasona(12)
        logt.append(n)
        pas.append(salasona)
 

    elif tehe==2:
       pas=input("Kirjutage oma parool: ")
       if any(c.islower() for c in pas) and any(c.isupper() for c in pas) and any(c.isdigit() for c in pas) and any(c in '.,:;!_*-+()/#¤%&' for c in pas):
            print("Olete loonud parooli")
            logt.append(n)
            pas.append(str(salasona))
       else:
            print("Viga!!!")
        
       
    return logt,pas
