import string
from random import choice


# создавать пустые списки логинов и паролей
loginiid = []
paroolid = []


# функция генерации случайного пароля
def salasona(k: int):
  sala=""
  for i in range(k):
   t=choice(string.ascii_letters) 
   num=choice([1,2,3,4,5,6,7,8,9,0])
   t_num=[t,str(num)]
   sala+=choice(t_num)
  return sala


# функция регистрации пользователя
def registreerimine():
    login = input("Sisesta oma login: ")
    if login in loginiid:
        print("See login on juba votud.")
        return
    salasona_valik = input("Kas sa tahad juhuslik salasone? (Y/N): ")
    if salasona_valik.lower() == 'y':
        parool = salasona(8)
        print(f"Sinu salasona: {parool}")
    else:
        while True:
            parool = input("Sisesta oma salasona: ")
            if any(char.isdigit() for char in parool) and any(char.islower() for char in parool) and any(char.isupper() for char in parool) and any(char in string.punctuation for char in parool):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
    loginiid.append(login)
    paroolid.append(parool)
    print("Registreerimine õnnetus!")


# функция авторизации пользователя
def autoriseerimine():
    login = input("Sisesta oma login: ")
    if login not in loginiid:
        print("See logini pole registreeritud.")
        return
    parool = input("Sisesta oma salasona: ")
    if parool != paroolid[loginiid.index(login)]:
        print("Vale salasona.")
        return
    print("Login õnnetus!")


# функция смены имени или пароля
def muuda():
    login = input("Sisesta oma login: ")
    if login not in loginiid:
        print("See nimi ei ole registreeritud.")
        return
    valik = input("Kas soovite muuta oma nime või parooli? (login/password): ")
    if valik.lower() == 'login':
        uus_login = input("Sisesta uue login: ")
        if uus_login in loginiid:
            print("See login on juba võtud.")
            return
        loginiid[loginiid.index(login)] = uus_login
        print("Login muudatus õnnetus.")
    elif valik.lower() == 'password':
        while True:
            uus_parool = input("Sisesta uue salasone: ")
            if any(char.isdigit() for char in uus_parool) and any(char.islower() for char in uus_parool) and any(char.isupper() for char in uus_parool) and any(char in string.punctuation for char in uus_parool):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
        paroolid[loginiid.index(login)] = uus_parool
        print("Salasone muudatus õnnetus.")
    else:
        print("Viga.")


# функция восстановления забытого пароля
def unustasin_parool():
    login = input("Наберите свой логин: ")
    if login not in loginiid:
        print("Вы не зарегистрированы.")
        return
    uus_parool = salasona(8)
    paroolid[loginiid.index(login)] = uus_parool
    print(f"Sinu uus parool on: {uus_parool}")


# функция выхода из системы
def logout():
    print("Sa logisid välja.")
    
