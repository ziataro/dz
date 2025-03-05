matrix = [['а', 'б', 'в', 'г', 'д', 'е'],
          ['ё', 'ж', 'з', 'и', 'й', 'к'],
          ['л', 'м', 'н', 'о', 'п', 'р'],
          ['с', 'т', 'у', 'ф', 'х', 'ц'],
          ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
          ['э', 'ю', 'я', '$', '%', '^'],
          ['*', ',', '!', '=', '.', ' ']]
word = input("Введите слово для шифровки(Внимание английские символы не будут учитыватсься):")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
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

some_text = polibiy(word,  False)
print(some_text)