import re
from math import sqrt
import string


# 1
def digits_of_number(num: int) -> str:
    lst = []
    for idx, d in enumerate(str(num)[::-1]):
        if idx != 0 and idx % 3 == 0:
            lst.append(' ')
        lst.append(d)

    num_with_pos = ''.join(lst[::-1])
    return num_with_pos


# 2
def snake_camel_switch(obj_name: str) -> str:
    lst = []
    # camel to snake
    if obj_name[0].isupper():
        for i in obj_name:
            if i.isupper():
                lst.append('_')
            lst.append(i.lower())

        return ''.join(lst[1:])

    # snake to camel
    else:
        lst.append(obj_name[0].upper())
        for idx, i in enumerate(obj_name):
            if idx == 0:
                continue
            elif i == '_' and idx != 0:
                lst.append(obj_name[idx+1].upper())
                continue
            elif obj_name[idx-1] == '_':
                continue
            lst.append(i)

        return ''.join(lst)


# 3
def roots_quadratic_equation(eq: str):
    # find coef a
    res_a = re.search("([-+]*)\s*(\d*)\**x\*\*2\s", eq)
    if res_a is None:
        return print("Введите квадратное уравнение")
    elif res_a.group(2) == "":
        a = int(res_a.group(1) + "1")
    else:
        a = int(res_a.group(1) + res_a.group(2))

    # find coef b
    res_b = re.search("\s([-+])\s(\d*)\**x\s", eq)
    if res_b is None:
        b = 0
    elif res_b.group(2) == "":
        b = int(res_b.group(1) + "1")
    else:
        b = int(res_b.group(1) + res_b.group(2))

    # find coef c
    res_c = re.search("\s([-+])\s(\d*)\s=", eq)
    if res_c is None:
        c = 0
    else:
        c = int(res_c.group(1) + res_c.group(2))
    print(c)

    # solving a quadratic equation
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / 2 * a
        x2 = (-b - sqrt(discriminant)) / 2 * a
        return print(f"x_1 = {x1}, x_12 = {x2}")

    elif discriminant == 0:
        x = (-b + sqrt(discriminant)) / 2 * a
        return print(f"x_1 = x_2 = {x}")

    else:
        return print("Уравнение не имеет действительных решений")


# 4
def caesars_cipher(word: str, num: int) -> str:
    lat_alphabet = string.ascii_lowercase
    kirill_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    word = word.lower()
    word_lst = word.strip()
    encrypted_word = ''

    if re.match('[a-z]', word):
        for char in word_lst:
            encrypted_word += lat_alphabet[(lat_alphabet.index(char) + num) % len(lat_alphabet)]

    elif re.match('[а-яё]', word):
        for char in word_lst:
            encrypted_word += kirill_alphabet[(kirill_alphabet.index(char) + num) % len(kirill_alphabet)]

    else:
        print("Слово не распознано")

    return encrypted_word


def caesars_cipher_decryption(word: str, num: int) -> str:
    lat_alphabet = string.ascii_lowercase
    kirill_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    word = word.lower()
    word_lst = word.strip()
    decrypted_word = ''

    if re.match('[a-z]', word):
        for char in word_lst:
            decrypted_word += lat_alphabet[(lat_alphabet.index(char) - num) % len(lat_alphabet)]

    elif re.match('[а-яё]', word):
        for char in word_lst:
            decrypted_word += kirill_alphabet[(kirill_alphabet.index(char) - num) % len(kirill_alphabet)]

    else:
        print("Слово не распознано")

    return decrypted_word
