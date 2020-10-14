def ask_password():
    key = False
    for i in range(3):
        s = input()
        if not key:
            if s == 'password':
                key = True
    if key:
        print('Пароль принят')
    else:
        print('В доступе отказано')
    return


ask_password()
