import csv

file_csv = []
csv_otchisleni_file = []
fileName = ''


# Открываем csv файл
def open_file():
    global file_csv
    global csv_otchisleni_file
    global fileName
    fileName = input('Название файла (по умолчанию data.csv): ')
    # Если файл не указан - задаём значение по умолчанию
    if (fileName == ''):
        fileName = 'data.csv'

    # Открываем файл
    try:
        with open(fileName, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                file_csv.append(row)
                with open('data_otchisleni.csv', "r", newline="", encoding="utf-8") as file: reader = csv.DictReader(
                    file, delimiter=';')
            for row in reader:
                csv_otchisleni_file.append(row)
        print('Файл открыт. Записей:', len(file_csv))
    # Если не получилось - выводим сообщение об ошибке
    except:
        print('Файл не получилось открыть!', sep='\n')

        # Добавление данных


def insert_data(fio, gender, age, tel, email, group, curs):
    global file_csv
    try:
        try:
            mx = max(file_csv, key=lambda x: int(x['ном']))
        except:
            mx = {'ном': 0}
        file_csv.append({'ном': int(mx['ном']) + 1, 'фио': fio, 'пол': gender,
                         'возраст': age, 'телефон': tel,
                         'почта': email, 'группа': group, 'курс': curs})
    except Exception as e:
        print('Ошибка при добавленнии новой записи: ', e, sep='\n')
        return
    print('Данные добавлены.')

    # Перевести на следующий курс


def go_to_next_curs():
    global file_csv
    try:
        for index, curs in enumerate(list(map(lambda x: x['курс'], file_csv))):
            if int(curs) == 5:
                student = file_csv[index]
                insert_otchisleni(student)
                drop_by_arg(student['ном'], 'ном')
            else:
                file_csv[index]['курс'] = int(curs) + 1
        print('Студенты переведены!')
    except Exception as e:
        print('Не получилось перевести на следующий курс: ', e, sep='\n')

        # Вывод совершеннолетних


def find_adults():
    global csvfile_csv_file
    print(*list(filter(lambda x: int(x['возраст']) >= 18, file_csv)))


# Запись отчисленных студентов


def insert_otchisleni(student):
    global csv_otchisleni_file
    try:
        csv_otchisleni_file.append(
            {'ном': student['ном'], 'фио': student['фио'], 'пол': student['пол'], 'возраст': student['возраст'],
             'телефон': student['телефон'], 'почта': student['почта'], 'группа': student['группа'],
             'курс': student['курс']})
    except Exception as e:
        print(e)
        pass


# Сводка по курсу/группе
def analytic(type, val):
    global file_csv
    print(f'Количество студентов: {len(list(filter(lambda x: x[type] == val, file_csv)))}')


# Сохранение отчисленных студентов
def save_otchisleni():
    global csv_otchisleni_file
    print(1)
    with open('data_otchisleni.csv', "w", encoding="utf-8", newline="") as file:
        columns = ['ном', 'фио', 'пол', 'возраст', 'телефон', 'почта', 'группа', 'курс']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_otchisleni_file)


# Сохранение
def save():
    global fileName
    global csv_otchisleni_file
    if (fileName == ''):
        print('Файл не выбран!')
        return
    try:
        with open(fileName, "w", encoding="utf-8", newline="") as file:
            columns = ['ном', 'фио', 'пол', 'возраст', 'телефон', 'почта',
                       'группа', 'курс']
            writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
            writer.writeheader()
            writer.writerows(file_csv)
            print("Данные сохранены!")
            if len(csv_otchisleni_file) > 0:
                save_otchisleni()
    except Exception as e:
        print('Ошибка при сохранении: ', e, sep='\n')

        # Удалить по аргументу


def drop_by_arg(val, col_name='фио'):
    global file_csv
    try:
        file_csv = list(filter(lambda x: x[col_name] != val, file_csv))
    except Exception as e:
        print(f'Строка со значением {val} поля {col_name} не найдена.')
        return
    print(f'Строка со значением "{val}" столбца "{col_name}" удалена.')


# Поиск
def find(val, col_name='фио'):
    try:
        print(*list(filter(lambda x: x[col_name] == val, file_csv)))
    except Exception as e:
        print('Данные не найдены: ', e, sep='\n')

        # Вывод совершеннолетних студентов
