# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
import glob

migrations = 'Migrations\\'
current_dir = os.path.dirname(os.path.abspath(__file__))
file_extension = '.css'

# print(current_dir)
migrations_dir = os.path.join(current_dir, migrations)
# print(migrations_dir)
if __name__ == '__main__':
    # ваша логика
    pass


a = glob.glob('Migrations/*.sql')
# print(a)
b = []
for i in range(len(a)):
    cuted_name = a[i].replace(migrations, '')
    cuted_name = cuted_name.replace(file_extension, '')
    b.append(cuted_name)
# print(b)

while True:
    result = []
    count = 0
    file_name = input('Enter the name of the "sql" file: ')
    print('------------------------------------------')
    for i in range(len(b)):
        if file_name in b[i]:
            result.append(b[i])
            find_file_path = os.path.join(migrations + b[i] + file_extension)
            print(find_file_path)
            count += 1      
        else:
            continue
#    print(result)
    print('------------------------------------------')
    print('Всего:', count)
    print('------------------------------------------')
    b = result