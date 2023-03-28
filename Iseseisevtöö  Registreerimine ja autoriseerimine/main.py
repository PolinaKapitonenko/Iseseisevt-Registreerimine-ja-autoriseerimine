from MyModule import registreerimine, autoriseerimine, muuda, unustasin_parool, logout

while True:
    print("Выбирите:")
    print("1. Регистрация")
    print("2. Авторизоваться")
    print("3. Сменить логин или пароль")
    print("4. Вы забыли свой пароль")
    print("5. Выйти")
    valik = input("Введите число (1-5): ")
    if valik == '1':
        registreerimine()
    elif valik == '2':
        autoriseerimine()
    elif valik == '3':
        muuda()
    elif valik == '4':
        unustasin_parool()
    elif valik == '5':
        logout()
        exit()
    else:
        print("Viga! Palun andke number 1st kuni 5ni.")