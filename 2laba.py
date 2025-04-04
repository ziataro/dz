# Массивы с данными верхних и нижних регистров русского языка и знаков препинания
ru_low = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
          'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
ru_high = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
           'У', 'Ф', 'Ч', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
punctuation = ['!', '"', '#', '$', '%', '&', "'", '(',
               ')', '*', '+', ',', '-', '.', '/',
               ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
               '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '—']

# Ввод текста для шифрования
word = input("Введите слово для шифровки(Внимание английские символы не будут учитыватсься):")


# Шифровка текста методом Цезаря
def ceaser(text_to_encrypt):
    great_string = ""
    for i in text_to_encrypt:
        for j in range(len(ru_low)):
            if i in ru_low[j]:
                if j == 0:
                    great_string += ru_low[32]
                    break
                great_string += ru_low[-j-1]
            if i in ru_high[j]:
                if j == 0:
                    great_string += ru_high[32]
                    break
                great_string += ru_high[-j-1]
        # Проверка и ввод всех пунктуационных символов
        if i in punctuation:
            great_string += i
    return great_string


choice = input("Хотите зашифровать или дешифровать текст? Введите ш/д для шифровки или дешифровки ")
if choice == "ш":

    # Вывод зашифрованного текста
    print("Зашифрованный текст:", ceaser(word))
elif choice == "д":
    # Вывод расшифрованного текста
    print("Расшифрованный текст:", ceaser(word))
else:
    print("Неверный формат ввода")