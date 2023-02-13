# Задача 1.=====
# На заводе «Кофейный» открывается новое кафе. Изначально есть некоторое количество
# кофейных зерен, молока и взбитых сливок.
# Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), которая
# возвращает напиток, который можно приготовить из имеющихся продуктов (ingredients).
# На вход функция принимает заранее неизвестное количество предпочтений посетителя.
# Все напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
# Бариста готовит наиболее предпочитаемый напиток из доступных.
# Для Эспрессо требуется: 1 порция кофейных зерен.
# Для Капучино требуется: 1 порция кофейных зерен и 3 порции молока.
# Для Маккиато требуется: 2 порции кофейных зерен и 1 порция молока.
# Для Кофе по-венски требуется: 1 порция кофейных зерен и 2 порции взбитых сливок.
# Для Латте Маккиато требуется: 1 порция кофейных зерен, 2 порции молока и 1 порция взбитых сливок.
# Для Кон Панна требуется: 1 порция кофейных зерен и 1 порция взбитых сливок.
# При приготовлении напитка ингредиенты расходуются.
# Если недостаточно ингредиентов, то вернуть сообщение: «К сожалению, не можем предложить Вам напиток»

print("Введите начальное количество порций ингридиентов: ")
ingredients = []
a = int(input("Кофейные зерна: "))
ingredients.append(a)
b = int(input("Молоко: "))
ingredients.append(b)
c = int(input("Взбитые сливки: "))
ingredients.append(c)
print(ingredients)

print(" ' Эспрессо - 1 ', ' Капучино - 2 ', ' Маккиато - 3 ', ' Кофе по-венски - 4 ', ' Латте Маккиато - 5 ',  ' Кон Панна - 6 '")
user_preferences = list(input(
    'Введите наиболее предпочитаемый напиток из доступных в порядке убывания (через пробел): ').split(' '))
print(user_preferences)


def choose_coffee(*preference):
    global ingredients
    for i in preference:
        if i == '1':
            if ingredients[0] >= 1:
                ingredients[0] -= 1
                return 'Эспрессо'
        if i == '2':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                ingredients[0] -= 1
                ingredients[1] -= 3
                return 'Капучино'
        if i == '3':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                ingredients[0] -= 2
                ingredients[1] -= 1
                return 'Маккиато'
        if i == '4':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                ingredients[0] -= 1
                ingredients[2] -= 2
                return 'Кофе по-венски'
        if i == '5':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[1] -= 2
                ingredients[2] -= 1
                return 'Латте Маккиато'
        if i == '6':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[2] -= 1
                return 'Кон Панна'
    return 'К сожалению, не можем предложить Вам напиток'


print(choose_coffee(*user_preferences))
print(choose_coffee(*user_preferences))
print(choose_coffee(*user_preferences))
print(choose_coffee(*user_preferences))


# Задача 2.=====
# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
# Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
# отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
# функция кодирует сдвиг алфавита на 3 позиции:
# А→Г,А→Г,
# Б→Д,Б→Д,
# В→Е,В→Е,
# ……
# Э→А,Э→А,
# Ю→Б,Ю→Б,
# Я→ВЯ→В
# Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны
# превращаться в маленькие, большие — в большие.
# Напишите также функцию декодирования decrypt_caesar(msg, shift), также
# использующую сдвиг по умолчанию. При написании функции декодирования используйте
# вашу функцию кодирования

# small_symbols = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# big_symbols = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


# def shift(text, symbols, n):
#     index = symbols.find(text)
#     if index + n < len(symbols):
#         return symbols[index + n]
#     else:
#         return symbols[(index + n) % len(symbols)]


# def back_shift(text, symbols, n):
#     index = symbols.find(text)
#     if index - n >= 0:
#         return symbols[index - n]
#     else:
#         return symbols[(index - n) % len(symbols)]


# def encrypt(text, n=3):
#     res = ""
#     for i in range(0, len(text)):
#         if text[i].isupper():
#             res += shift(text[i], big_symbols, n)
#         elif text[i].islower():
#             res += shift(text[i], small_symbols, n)
#         else:
#             res += text[i]
#     return res


# def decrypt(text, n=3):
#     res = ""
#     for i in range(0, len(text)):
#         if text[i].isupper():
#             res += back_shift(text[i], big_symbols, n)
#         elif text[i].islower():
#             res += back_shift(text[i], small_symbols, n)
#         else:
#             res += text[i]
#     return res


# str = encrypt(input())
# print(str)
# print(decrypt(str))
