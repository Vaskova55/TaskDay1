from data_csv import open_file, insert_data, drop_by_arg, find, \
    go_to_next_curs, find_adults, analytic, to_string, save

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
        go_to_next_curs()
    elif command == '6':
        find_adults()
    elif command == '7':
        type = input('Курс или группа: ')
        if (type.lower() == 'курс'):
            val = input('Какой: ')
        elif (type.lower() == 'группа'):
            val = input('Какая: ')
        else:
            print('Неверно указан тип!')
            continue
        analytic(type.lower(), val)
    elif command == '8':
        to_string()
    elif command == '9':
        save()
    elif command == '0':
        showMenu()
    elif command == 'exit':
        break
    else:
        print('Неверная команда, попробуйте ещё раз', '0: Назад в меню', sep='\n')