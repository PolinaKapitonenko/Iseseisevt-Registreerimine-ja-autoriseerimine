from random import*
import string
def salasona(k: int):
    sala=""
    for i in range(k):
        t=choice(string.ascii_letters)
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus

def Registereerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi:")
    v=int(input("1-Ese koostan parooli/n2-Arvuti genireebib/n"))
    if v==1:
        pass
    else:
        salasona=salasona(5)
        l.append(nimi)
        p.append(salasona)
        return l,p


def Autoriseerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi:")
    salasona=input("Sisesta oma salasõna:")
    if nimi in l:
        ind=l.index(nimi)
        if salasona==p[ind]:
            print("Tere tulemast!")
        else:
            print("Vale salasõma!")
    else:
        print("Nimi ei ole nimekirjas!")