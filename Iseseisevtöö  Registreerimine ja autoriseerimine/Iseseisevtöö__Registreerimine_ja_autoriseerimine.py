from math import*
from random import*
from module1  import*


l=["Polina"]
p=["12345"]
while True:
    v=int(input("1-Regisreerimine/n2-Aurotiseerimine/n3-Välja"))
    if v==1:
        l,p=Registereerimine(l,p)
        pass
    elif v==2:
        Autoriseerimine()
    elif v==3:
        break
    else:
        print("tee õige valik")
         
