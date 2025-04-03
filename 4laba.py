from matrix_generator import matrix_generate, matrix_shuffle, matrix
import locale

matrix_generate()
InMassive = 0
adfgx_massive = {0:'A', 1:'D', 2:'F', 3:'V', 4:'G', 5:"X"}
def validate_russian_key(key, min_length=5):
    russian_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    key = key.upper().replace('Ё', 'Е')
    filtered_key = [char for char in key if char in russian_alphabet]
    clean_key = ''.join(filtered_key)
    if len(clean_key) < min_length:
        return False, f"Ключ слишком короткий. Минимум {min_length} русских букв."
    duplicates = set([char for char in clean_key if clean_key.count(char) > 1])
    if duplicates:
        return False, f"Повторяющиеся буквы: {', '.join(duplicates)}"
    
    return True, "Ключ корректен"
is_correct = False
while(not is_correct):
    key = input("Введит ключ для шифрования")
    print(validate_russian_key(key)[1])
    is_correct = validate_russian_key(key)[0]
word = input("Введите слово для шифровки:")
for i in range(6):
    for j in range(6):
        print(matrix[i][j], end=' ')
    print()

def find_element(arr, target):
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            if value == target:
                return i,j

def adfgx(word):
    matrix_with_key = []
    first_act = []
    two_act = {}
    for char in word:
        first_act += find_element(matrix, char)
    for i in range(len(first_act)):
        first_act[i] = adfgx_massive.get(first_act[i])
    for i in range(len(first_act)//len(key)):
        matrix_with_key.append([])
    for i in range(len(first_act)//len(key)):
        for j in range(len(key)):
            matrix_with_key[i].append(first_act[j + (i * 6)])
    transposed = list(zip(*matrix_with_key))
    for i, column in enumerate(transposed, 1):
        conjoined = "".join(column)
        two_act.update({f"{key[i-1]}":f"{conjoined}"})
    sorted_dict = {k: two_act[k] for k in sorted(two_act)}
    execution = list(sorted_dict.values())
    execution = "".join(execution)
    return execution


def decryptor_adfgx(ciphertext):

    reverse_adfgx = {'A': 0, 'D': 1, 'F': 2, 'V': 3, 'G': 4, 'X': 5}

    key_len = len(key)
    chunk_size = len(ciphertext) // key_len
    cipher_chunks = [ciphertext[i * chunk_size:(i + 1) * chunk_size] for i in range(key_len)]

    sorted_key = sorted(key)
    column_order = [key.index(c) for c in sorted_key]
    reordered_columns = [cipher_chunks[i] for i in column_order]

    transposed = list(zip(*reordered_columns))
    flattened = [item for sublist in transposed for item in sublist]

    pairs = [flattened[i:i + 2] for i in range(0, len(flattened), 2)]

    decrypted = []
    for pair in pairs:
        if len(pair) == 2:
            row = reverse_adfgx[pair[0]]
            col = reverse_adfgx[pair[1]]
            decrypted.append(matrix[row][col])

    plaintext = ''.join(decrypted)
    if plaintext.endswith('X'):
        plaintext = plaintext[:-1]
    return plaintext




while True:
    choice = input("Хотите зашифровать или дешифровать текст? Введите ш/д для шифровки или дешифровки: ")
    if choice == "ш":
        # Вывод зашифрованного текста
        print("Зашифрованный текст:", adfgx(word))
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
        print("Расшифрованный текст:", decryptor_adfgx(word))
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