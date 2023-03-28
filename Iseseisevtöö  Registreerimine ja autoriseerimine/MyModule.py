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
    login = input("Введите ваш логин: ")
    if login in loginiid:
        print("Этот логин уже занят.")
        return
    salasona_valik = input("Вы хотите случайный пароль? (Y/N): ")
    if salasona_valik.lower() == 'y':
        parool = salasona(8)
        print(f"Ваш пароль: {parool}")
    else:
        while True:
            parool = input("Введите ваш пароль: ")
            if any(char.isdigit() for char in parool) and any(char.islower() for char in parool) and any(char.isupper() for char in parool) and any(char in string.punctuation for char in parool):
                break
            else:
                print("Ваш пароль должен содержать как минимум одну цифру, одну строчную букву, одну прописную букву и один специальный символ..")
    loginiid.append(login)
    paroolid.append(parool)
    print("Регистрация прошла успешно!")


# функция авторизации пользователя
def autoriseerimine():
    login = input("Введите ваш логин: ")
    if login not in loginiid:
        print("Этот логин еще не зарегистрирован.")
        return
    parool = input("Введите ваш пароль: ")
    if parool != paroolid[loginiid.index(login)]:
        print("Неправильный пароль.")
        return
    print("Авторизация прошла успешно!")


# функция смены имени или пароля
def muuda():
    login = input("Введите ваш логин: ")
    if login not in loginiid:
        print("Это имя не зарегистрировано.")
        return
    valik = input("Вы хотите изменить свое имя или пароль? (Логин/Пароль): ")
    if valik.lower() == 'логин':
        uus_login = input("Введите новый логин: ")
        if uus_login in loginiid:
            print("Такой логин уже занят.")
            return
        loginiid[loginiid.index(login)] = uus_login
        print("Успешно со сменой логина.")
    elif valik.lower() == 'пароль':
        while True:
            uus_parool = input("Введите новый пароль: ")
            if any(char.isdigit() for char in uus_parool) and any(char.islower() for char in uus_parool) and any(char.isupper() for char in uus_parool) and any(char in string.punctuation for char in uus_parool):
                break
            else:
                print("Ваш пароль должен содержать как минимум одну цифру, одну строчную букву, одну прописную букву и один специальный символ.")
                return
        paroolid[loginiid.index(login)] = uus_parool
        print("Успешно со сменой логина.")
    else:
        print("Ошибка.")


# функция восстановления забытого пароля
def unustasin_parool():
    login = input("Наберите свой логин: ")
    if login not in loginiid:
        print("Вы не зарегистрированы.")
        return
    uus_parool = salasona(8)
    paroolid[loginiid.index(login)] = uus_parool
    print(f"Ваш новый пароль: {uus_parool}")


# функция выхода из системы
def logout():
    print("Выйти из системы.")
    
