from matrix_generator import matrix_generate, matrix_shuffle, matrix

matrix_generate()
InMassive = 0
while True:
    # Ввод текста для шифрования
    word = input("Введите слово для шифровки:")
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
                            encrypted_text += matrix[i + 1][j]
                        break
                    else:
                        if i + 1 > len(matrix):
                            encrypted_text += matrix[-i][j]
                        else:
                            encrypted_text += matrix[i - 1][j]
                        break
    return encrypted_text


while True:
    choice = input("Хотите зашифровать или дешифровать текст? Введите ш/д для шифровки или дешифровки: ")
    if choice == "ш":
        # Вывод зашифрованного текста
        print("Зашифрованный текст:", polibiy(word, True))
        choice_shuffle = input("Хотите случайно отсортировать матрицу?д/н: ")
        while True:
            if choice_shuffle == "н":
                break
            elif choice_shuffle == "д":
                print("Новый вид матрицы:")
                matrix_shuffle()
                break
            else:
                print("Неверный формат ввода")
        break
    elif choice == "д":
        # Вывод расшифрованного текста
        print("Расшифрованный текст:", polibiy(word, False))
        choice_shuffle = input("Хотите случайно отсортировать матрицу?д/н: ")
        while True:
            if choice_shuffle == "н":
                break
            elif choice_shuffle == "д":
                print("Новый вид матрицы:")
                matrix_shuffle()
                break
            else:
                print("Неверный формат ввода")
        break
    else:
        print("Неверный формат ввода")
