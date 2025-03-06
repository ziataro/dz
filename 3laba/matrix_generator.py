import random
import re

matrix = [['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', '']]

matrix_to_txt = ''
pattern = r'^(.{6} .{6} .{6} .{6} .{6} .{6})$'
while True:
    choice = input("Вы хотите создать свой файл с расширением .txt или открыть уже готовый?\n"
                   " Для 1 нажмите с, для 2 соответственно о: ")
    if choice == "o" or choice == "о":
        while True:
            try:
                file_name = input(
                    "Введите путь и название файла формата .txt с готовой матрицей: ")
                f = open(f'{file_name}', 'r', encoding='utf-8')
                break
            except FileNotFoundError or PermissionError:
                print("Файл не найден, если такой файл существует попробуйте ввести его полный путь \n"
                      r"пример: C:\Users\cisle\PycharmProjects\dz\3laba\matrix.txt")
        break
    elif choice == "c" or choice == "с":
        fill = input("Введите название файла для записи \n"
                     "пример: example.txt: ")
        while True:
            with open(fill, 'w+', encoding='utf-8') as file:
                file.write(input("введите содержание матрицы 6 на 6 пример записи: \n"
                                 "' дгеабв ёкжйиз мпнлро фхцуст щчьъыш юяэ.,N ' , где пробелы разделение на столбцы и "
                                 "N это"
                                 " пробел: "))
                file.close()
            with open(fill, 'r+', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()  # Убираем лишние пробелы и переносы строк
                    if re.match(pattern, line):
                        print("Файл с матрицей создан!")
                        break
                    else:
                        print("Неверный формат матрицы")
                        file.truncate(0)

        break
    else:
        print("Неверный формат ввода")


def matrix_generate():
    string_matrix = f.readline()
    string_matrix = string_matrix.split()
    for i in range(6):
        for j in range(0, 6):
            matrix[i][j] = string_matrix[i][j]
            if matrix[i][j] == 'N':
                matrix[i][j] = ' '
    f.close()


def matrix_shuffle(matrix_to_txt=''):
    for i in range(6):
        random.shuffle(matrix[i])
    for i in range(6):
        for j in range(0, 6):
            if matrix[i][j] == ' ':
                matrix[i][j] = 'N'
            print(matrix[i][j], end=' ')
        print()
    for i in range(6):
        matrix_to_txt += ''.join(matrix[i])
        matrix_to_txt += ' '
    with open(f'{file_name}', 'w', encoding='utf-8') as f:
        f.write(matrix_to_txt)
        f.close()
