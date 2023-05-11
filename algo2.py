# алгоритм шифра простой замены с открытым ключом

# мы используем модуль random для случайной замены символов
import random

# Этот код реализует алгоритм нахождения наибольшего общего делителя (НОД) двух целых чисел a и b.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# функция для нахождения мультипликативно обратного элемента d для заданного числа e в кольце вычетов по модулю phi.
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

# функция generate_keypair нужна для генерации пары ключей - публичного и приватного
# Публичный ключ содержит два числа - модуль n и открытую экспоненту e, а приватный ключ содержит те же числа, но с закрытой экспонентой d.
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((n, e), (n, d))

# Функция encrypt использует публичный ключ для шифрования сообщения
def encrypt(public_key, plaintext):
    n, e = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Функция decrypt использует приватный ключ для дешифрования
def decrypt(private_key, ciphertext):
    n, d = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Обе функции используют операцию возведения в степень по модулю n, чтобы зашифровать или расшифровать каждый символ сообщения.

# В этом примере использованы простые числа p и q, но в реальных приложениях используются гораздо большие простые числа, чтобы обеспечить безопасность шифрования.
p = 61
q = 53

public, private = generate_keypair(p, q)

message = "Hello, world!"
encrypted_message = encrypt(public, message)
decrypted_message = decrypt(private, encrypted_message)

print("Public key: ", public)
print("Private key: ", private)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)
