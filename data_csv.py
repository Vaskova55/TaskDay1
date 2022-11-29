import csv

file_csv = []
fileName = ''


# Открываем csv файл
def open_file():
    global file_csv
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

    # Сохранение


def save():
    global fileName
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
