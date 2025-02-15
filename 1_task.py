"""
1 Задача "Генератор паролей"
Написать программу, которая генерирует надежные пароли заданной длины, включающие:
Прописные и строчные буквы
Цифры
Специальные символы
Пароль должен удовлетворять следующим требованиям безопасности:
Минимум одна заглавная буква
Минимум одна цифра
Минимум один специальный символ
"""

# сначала напишу процедурно программу, затем оберну в функцию
import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_symbols = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
length = int(input("Введите длину пароля: "))
# random.choice(list) – выбирает случайный элемент из списка
# random.randint(a, b) – генерирует случайное целое число в диапазоне от a до b включ.
# password_dict = {i for i in range(0, length)} – так не работает, словарь не список
# инициализируем пустой словарь с индексами:
# password_dict = dict.fromkeys(range(0, length), None) 
password_dict = dict()

first_constraint = random.choice(letters.upper())
first_constraint_index = random.randint(0, length - 1)
password_dict[first_constraint_index] = first_constraint

# from random import choice – случайное число из диапазона, минус некот. знач-я
# print(choice([i for i in range(0,9) if i not in [2,5,7]]))
second_constraint = random.choice(numbers)
second_constraint_index = random.choice([i for i in range(0, length) if i not in password_dict.keys()])
password_dict[second_constraint_index] = second_constraint

third_constraint = random.choice(special_symbols)
third_constraint_index = random.choice([i for i in range(0, length) if i not in password_dict.keys()])
password_dict[third_constraint_index] = third_constraint

remaining_symbols = letters + numbers + special_symbols

# for i, v in password_dict:
#     if v is None: 
#         v = random.choice(remaining_symbols)
#     else:
#         continue

# Также с помощью dict comprehension можно, например, создать словарь, где ключи — строки, а значения — их длины: 1
# word_lengths = {word: len(word) for word in words}
# print(word_lengths)  # Вывод: {'apple': 5, 'banana': 6, 'cherry': 6}

# password = {i: random.choice(remaining_symbols) for i in range(0, length) if 
#              in password_dict.keys() if password_dict[i] is None password_dict[i] = random.choice(remaining_symbols) else pass}
# print(str(password_dict.values()))

# пытался работать со словарем, но проще сделать через список:
# я хочу просто заполнить список случайными элементами, а затем заменить на гарантированные constraint

# пример list comprehension
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares_of_even = [x ** 2 for x in numbers if x % 2 == 0]
# print(squares_of_even)

password = [random.choice(remaining_symbols) for _ in range(length)]
for i in password_dict.keys():
    password[i] = password_dict[i]

print(password_dict)
print("".join(password))
