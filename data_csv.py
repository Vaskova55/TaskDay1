import csv

file_csv = []

# Открываем csv файл
def open_file():
    global file_csv
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
        print('Файл не получилось открыть!', 'Проверьте наличие файла', sep='\n')