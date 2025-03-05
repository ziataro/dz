import random
matrix = [['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', ''],
          ['', '', '', '', '', '']]
InMassive = 0
matrix_to_txt = ''
f = open('3laba/matrix.txt', 'r', encoding='utf-8')
string_matrix = f.readline()
string_matrix = string_matrix.split()
for i in range(6):
    for j in range(0, 6):
        matrix[i][j] = string_matrix[i][j]
        if matrix[i][j] == 'N':
            matrix[i][j] = ' '

while True:
    # Ввод текста для шифрования
    word = input("Введите слово для шифровки(Внимание английские символы не будут учитываться):")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in word:
                if k in matrix[i][j]:
                    InMassive += 1
    if InMassive == len(word):
        break
    else:
        print("Неверный формат ввода")
        InMassive = 0

for i in range(6):
    for j in range(6):
        print(matrix[i][j], end=' ')
    print()
def polibiy(text, chipher):
    encrypted_text = ""
    for word in text:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if word == matrix[i][j]:
                    if chipher:
                        if i + 1 >= len(matrix):
                            encrypted_text += matrix[0][j]
                        else:
                            encrypted_text += matrix[i+1][j]
                        break
                    else:
                        if i + 1 > len(matrix):
                            encrypted_text += matrix[-i][j]
                        else:
                            encrypted_text += matrix[i-1][j]
                        break
    return encrypted_text

while True:
    choice = input("Хотите зашифровать или дешифровать текст? Введите ш/д для шифровки или дешифровки ")
    if choice == "ш":
    # Вывод зашифрованного текста
        print("Зашифрованный текст:", polibiy(word, True))
        break
    elif choice == "д":
        # Вывод расшифрованного текста
        print("Расшифрованный текст:", polibiy(word, False))
        for i in range(6):
            random.shuffle(matrix[i])
        for i in range(6):
            for j in range(0, 6):
                if matrix[i][j] == ' ':
                    matrix[i][j] = 'N'
        for i in range(6):
            matrix_to_txt += ''.join(matrix[i])
            matrix_to_txt += ' '
        with open('3laba/matrix.txt', 'w',  encoding='utf-8') as f:
            f.write(matrix_to_txt)
        break
    else:
        print("Неверный формат ввода")
f.close()