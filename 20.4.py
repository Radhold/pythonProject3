def hello(name):
    print(f'Здравсвуйте, {name}! Вашу карту ищут...')


def search_card(name):
    if name in base:
        print(f'Ваша карта с номером {base.index(name) + 1} найдена')
    else:
        print('Ваша карта не найдена')


base = ['Иван', 'Юлия Иванкова']
hello('Иван')
search_card('Иван')
hello('Юлия Иванова')
search_card('Юлия Иванова')
