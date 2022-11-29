menu = {
    '1': 'Открыть файл',
    '2': 'Добавить',
    '3': 'Удалить',
    '4': 'Найти',
    '5': 'Перевести на следующий курс',
    '6': 'Вывести совершеннолетних студентов',
    '7': 'Вывести информацию по количеству студентов',
    '8': 'Вывести записи',
    '9': 'Сохранить в файл',
    '0': 'Назад в меню',
    'exit': 'Выход'
}

# Вывод меню
def showMenu():
    print('\n'.join([f'{key}: {value}' for key, value in menu.items()]))

showMenu()

while True:
    command = input()
    if command == '1':
        print(1)
    elif command == '2':
        print(2)
    elif command == '3':
        print(3)
    elif command == '4':
        print(4)
    elif command == '5':
        print(5)
    elif command == '6':
        print(6)
    elif command == '7':
        print(7)
    elif command == '8':
        print(8)
    elif command == '9':
        print(9)
    elif command == '0':
        showMenu()
    elif command == 'exit':
        break
    else:
        print('Неверная команда, попробуйте ещё раз', '0: Назад в меню', sep='\n')