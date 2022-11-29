from data_csv import open_file, insert_data, drop_by_arg, find, save

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
        open_file()
    elif command == '2':
        insert_data(input('ФИО: '), input('Пол: '), int(input('Возраст: ')), input('Телефон: '), input('Почта: '), input('Группа: '), input('Курс: '))
    elif command == '3':
        col = input('Колонка: ')
        val = input('Значение: ')
        drop_by_arg(val, col_name=col)
    elif command == '4':
        col = input('Колонка: ')
        val = input('Значение: ')
        find(val, col_name=col)
    elif command == '5':
        print(5)
    elif command == '6':
        print(6)
    elif command == '7':
        print(7)
    elif command == '8':
        print(8)
    elif command == '9':
        save()
    elif command == '0':
        showMenu()
    elif command == 'exit':
        break
    else:
        print('Неверная команда, попробуйте ещё раз', '0: Назад в меню', sep='\n')