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

# функция регистрации пользователя
def registerimine():
    login = input("Sisesta oma login: ")
    if login in logins:
        print("See login on juba votud.")
        return
    salasona_valik = input("Kas sa tahad juhuslik salasone? (Y/N): ")
    if salasona_valik.lower() == 'y':
        password = salasona(8)
        print(f"Sinu salasona: {password}")
    else:
        while True:
            password = input("Sisesta oma salasona: ")
            if any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
    logins.append(login)
    passwords.append(password)
    print("Registreerimine õnnetus!")

# функция авторизации пользователя
def autoreserimine():
    login = input("Sisesta oma login: ")
    if login not in logins:
        print("See logini pole registreeritud.")
        return
    password = input("Sisesta oma salasona: ")
    if password != passwords[logins.index(login)]:
        print("Vale salasona.")
        return
    print("Login õnnetus!")

# функция смены имени или пароля
def muuta():
    login = input("Sisesta oma login: ")
    if login not in logins:
        print("See nimi ei ole registreeritud.")
        return
    valik = input("Kas soovite muuta oma nime või parooli? (login/password): ")
    if valik.lower() == 'login':
        new_login = input("Sisesta uue login: ")
        if new_login in logins:
            print("See login on juba võtud.")
            return
        logins[logins.index(login)] = new_login
        print("Login muudatus õnnetus.")
    elif valik.lower() == 'password':
        while True:
            new_password = input("Sisesta uue salasone: ")
            if any(char.isdigit() for char in new_password) and any(char.islower() for char in new_password) and any(char.isupper() for char in new_password) and any(char in string.punctuation for char in new_password):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
        passwords[logins.index(login)] = new_password
        print("Salasone muudatus õnnetus.")
    else:
        print("Viga.")

# функция восстановления забытого пароля
def Unustasid parooli():
    login = input("Наберите свой логин: ")
    if login not in logins:
        print("Вы не зарегистрированы.")
        return
    new_password = salasona(8)
    passwords[logins.index(login)] = new_password
    print(f"Sinu uus parool on: {new_password}")


# функция выхода из системы
def Logivälja():
    print("Sa logisid välja.")
    
    


        
   
