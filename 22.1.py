def encrypt_caesar(m, s):
    counter = -1
    a = []
    for i in m:
        a.append(i)
    for i in a:
        counter += 1
        if ord(i) in range(1072, 1104):
            a[counter] = chr(1072 + (ord(i) + s + 32) % 1072 % 32)
        elif ord(i) in range(1040, 1072):
            a[counter] = chr(1040 + (ord(i) + s + 32) % 1040 % 32)
    return ''.join(a)


def decrypt_caesar(m, s):
    return encrypt_caesar(m, -s)


print(ord('а'), ord('м'))
print(ord('б'), ord('ь'))
print(ord('ё'), chr(11))
msg = 'Да здравствует салат Цезарь!'
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
