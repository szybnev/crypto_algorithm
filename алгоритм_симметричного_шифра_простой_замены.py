# мы используем модуль string для получения алфавита, который затем используется для создания ключевой таблицы замены
import string
# мы используем модуль random для случайного перемещения символов текста
import random

# Функция create_key() создает случайный ключ, перемешивая буквы алфавита
def create_key():
    # Создаем ключевую таблицу замены
    alphabet = list(string.ascii_lowercase)
    key = list(string.ascii_lowercase)
    random.shuffle(key)
    key = ''.join(key)
    return key

# Функция encrypt() использует ключ для шифрования сообщения
def encrypt(message, key):
    encrypted_message = ''
    for letter in message.lower():
        if letter in string.ascii_lowercase:
            index = string.ascii_lowercase.index(letter)
            encrypted_message += key[index]
        else:
            encrypted_message += letter
    return encrypted_message

# Функция decrypt() использует ту же таблицу замены для дешифровки сообщения
def decrypt(message, key):
    decrypted_message = ''
    for letter in message.lower():
        if letter in string.ascii_lowercase:
            index = key.index(letter)
            decrypted_message += string.ascii_lowercase[index]
        else:
            decrypted_message += letter
    return decrypted_message

# мы выводим исходное сообщение, зашифрованное сообщение и дешифрованное сообщение
key = create_key()
message = "Hello, world!"
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
