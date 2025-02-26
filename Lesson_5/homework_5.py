import json
import logging


import pytest
from assertpy import assert_that

from Lesson_5 import data1

# people_records = [
#   ('John', 'Doe', 28, 'Engineer', 'New York'),
#   ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
#   ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
#   ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
#   ('Michael', 'Brown', 22, 'Student', 'Seattle'),
#   ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
#   ('David', 'Miller', 33, 'Software Developer', 'Austin'),
#   ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
#   ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
#   ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
#   ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
#   ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
#   ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
#   ('Ava', 'White', 42, 'Journalist', 'San Diego'),
#   ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
# ]
#
# new_record = ('Serhii', 'White', 42, 'Journalist', 'San Diego')
# people_records.insert(1, new_record)
#
# people_records[1], people_records[5] = people_records[5], people_records[1]
# for record in people_records:
#   print(record)
#
# indices_to_check = [6, 10, 13]
#
# for index in indices_to_check:
#     age = people_records[index][2]
#     print(f"Person at index {index} has age >= 30: {age >= 30}")
#
#
#
#
# # У нас є search_criteria як кортеж ( year>= , engine_volume >= , price<=)
# # Автомобілі повинні бути відсортовані за зростанням ціни.
# # Ми повинні вивести до 5 (п'яти) перших знайдених елементів
# car_data = {
#   'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
#   'Audi': ('black', 2020, 2.0, 'sedan', 55000),
#   'BMW': ('white', 2018, 3.0, 'suv', 70000),
#   'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
#   'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
#   'Honda': ('red', 2017, 1.5, 'sedan', 30000),
#   'Ford': ('green', 2019, 2.3, 'suv', 40000),
#   'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
#   'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
#   'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
#   'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
#   'Kia': ('white', 2020, 2.0, 'sedan', 28000),
#   'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
#   'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
#   'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
#   'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
#   'Jeep': ('green', 2021, 3.0, 'suv', 50000),
#   'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
#   'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
#   'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
#   'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
#   'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
#   'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
#   'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
#   'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
#   'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
#   'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
#   'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
#   'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
#   'Acura': ('white', 2017, 2.4, 'suv', 40000),
#   'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
#   'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
#   'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
#   'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
#   'Ram': ('black', 2019, 5.7, 'pickup', 40000),
#   'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
#   'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
#   'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
#   'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
# }
# search_criteria = (2017, 1.6, 36000)
#
# filtered_cars = [
#     (car, data) for car, data in car_data.items()
#     if data[1] >= search_criteria[0]
#     and data[2] >= search_criteria[1]
#     and data[4] <= search_criteria[2]
# ]
#
# sorted_cars = sorted(filtered_cars, key=lambda x: x[1][4])
#
# for car in sorted_cars[:5]:
#     print(car)
#

# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль
# True, інакше - False. Строку отримати за допомогою функції input()

# string_input = input()
# numbers_of_uniqe_chars = set(char for char in string_input)
# print(len(numbers_of_uniqe_chars))
# if len(numbers_of_uniqe_chars) > 10:
#     print(True)
# else:
#     print(False)

# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

# char = 'h'
# while True:
#     string_input = input()
#     if 'h' in string_input.lower():
#         print('we found h')
#         break
#     else:
#         print('we didnt found h')

# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# list2 = []
# for x in lst1:
#   if type(x) is str:
#       list2.append(x)
# print(list2)

# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

# list3 = [4,5,7,3,4,2,3]
# list4 = [x for x in list3 if x%2 ==0]
# print(sum(list4))

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# def multiplication_table(number):
#     multiplier = 1
#
#     while multiplier <= 25:
#         result = number * multiplier
#         if  result > 25:
#             break
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))
#
#         multiplier += 1
#
# multiplication_table(7)



# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
# def sum_of_two_fingers(a,b):
#   return a+b;
#
# result = sum_of_two_fingers(7,4)
# print(result)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
# list_of_fingers = [4,3,8,5]
# def avg_of_fingers(some_function):
#     result = sum(some_function)/len(some_function)
#     return result
#
# print(avg_of_fingers(list_of_fingers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
#
# some_string :str = 'Rest'
# reversed_string : str = (some_string[::-1])
# print(reversed_string)
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
# list_of_words = ['Stuard','Enthony','John','Richardo']
# def longest_word_function(some_list):
#     for x in some_list:
#         max_value = max(list_of_words,key=len)
#         return max_value
# result = longest_word_function(list_of_words)
# print(result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
# def find_substring(str1, str2):
#     if (str1.find(str2)):
#         index = str1.find(str2)
#         return index
#     else:
#         return -1
#
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль
# True, інакше - False. Строку отримати за допомогою функції input()

# def check_unique_characters():
#     user_input = input("Введіть рядок: ")
#
#     unique_chars = set(user_input)
#
#     if len(unique_chars) > 10:
#         print(True)
#     else:
#         print(False)
#
# check_unique_characters()


# def compare_grades(grades1, grades2):
#   difference_dict = {}
#   for student in grades1:
#     if student in grades2:
#       difference = grades1[student] - grades2[student]
#       difference_dict[student] = difference
#
#   return difference_dict
#
#
# # Приклад використання
# grades_1 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78}
# grades_2 = {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80}
#
# result = compare_grades(grades_1, grades_2)
# print(result)  # Виведе: {'Анна Коваленко': -2, 'Олег Петров': -2, 'Ірина Сидорова': -2}


# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

#
# def sum_numbers_in_string(s):
#     try:
#         # Розбиваємо рядок на елементи за комами
#         elements = s.split(',')
#         total_sum = 0
#
#         for element in elements:
#             # Перевіряємо, чи є елемент числом
#             total_sum += int(element)  # Якщо не число, спрацює виключення
#         return total_sum
#     except ValueError:
#         # Якщо не вдається перетворити на ціле число, ловимо помилку
#         return "Не можу це зробити!"
#
# # Список рядків
# some_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
#
# # Обробляємо кожен елемент списку
# for x in some_list:
#     result = sum_numbers_in_string(x)
#     print(result)




#     sum_figures = sum(x)
#     print(sum_figures)
#         if x is not int:
#             raise ValueError
#
# except ValueError as e:
#     print(f"Не можу це зробити! {e}")

# import logging
# import unittest
#
# # Налаштування логера
# logging.basicConfig(
#     filename='test_log.log',
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# class TestLogger(unittest.TestCase):
#     def setUp(self):
#         # Створення додаткового обробника для консольного виведення
#         self.console_handler = logging.StreamHandler()
#         self.console_handler.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#         self.console_handler.setFormatter(formatter)
#         logging.getLogger().addHandler(self.console_handler)
#
#     def test_success_status(self):
#         logging.info("Test started: Success status")
#         log_event('Serhii', 'success')
#         logging.info("Test finished")
#
#     def tearDown(self):
#         # Видалення обробника після тесту
#         logging.getLogger().removeHandler(self.console_handler)
#
# def log_event(username: str, status: str):
#     log_message = f"Login event - Username: {username}, Status: {status}"
#     if status == "success":
#         logging.info(log_message)
#     elif status == "expired":
#         logging.warning(log_message)
#     else:
#         logging.error(log_message)
#
# if __name__ == '__main__':
#     unittest.main()
#
# some_string = 'good Bad UGLY'
# print(some_string.title())

# class Test():
#     def word_count(text: str) -> int:
#         # Розбиваємо рядок на слова і повертаємо кількість слів
#         return len(text.split())
#     #
    # def test_with_word_count(self):
    #     several_words: str = 'good Bad UGLY'
    #     result = Test.word_count(several_words)
    #     return print(f" Number of words {result}")


# Напишіть функцію concatenate_strings,
# яка приймає список стрінгових значень і об(''
#      'єднує їх у один рядок через вказаний символ.'
#      ' Напишіть тести для перевірки роботу функції на різних вхідних текстах.)

    # def concatenate_strings(listt:list[str]) -> str:
    #
    #     for x in listt:
    #         new_string: str = ','.join(listt)
    #         return new_string
    #
    # def concatenate_strings(listt: list[str], separator: str = ',') -> str:
    #     # Використовуємо join для об'єднання рядків у список через вказаний роздільник
    #     return separator.join(listt)
    #
    # def test_concatenate_strings_with_comma(self):
    #     # Тест з роздільником за замовчуванням (кома)
    #     some_list = ['Some', 'words', 'that']
    #     result = Test.concatenate_strings(some_list)
    #     assert result == 'Some,words,that'
    #
    # def test_concatenate_strings_with_space(self):
    #     # Тест з іншим роздільником (пробіл)
    #     some_list = ['Some', 'words', 'that']
    #     result = Test.concatenate_strings(some_list, ' ')
    #     assert result == 'Some words that'
    #
    # def test_concatenate_strings_empty_list(self):
    #     # Тест для порожнього списку
    #     some_list = []
    #     result =  Test.concatenate_strings(some_list)
    #     assert result == ''  # Порожній список дає порожній рядок
    #
    # def test_concatenate_strings_single_element(self):
    #     # Тест для списку з одним елементом
    #     some_list = ['OnlyOne']
    #     result =  Test.concatenate_strings(some_list)
    #     assert result == 'OnlyOne'  # Один елемент не змінюється

        # def four_functions(text:str):
        #     if text.upper():
        #         return text
        #     elif text.lower():
        #         return text
        #     elif text.startswith('Text'):
        #         return text
        #     elif text.endswith('end'):
        #         return text
        #     else:
        #         return print('MY OWN ERROR')

# def string_methods_operations(input_string: str):
#     # Викликаємо різні методи над рядком і повертаємо результати у вигляді словника
#     return {
#         "upper": input_string.upper(),            # Перетворює всі літери на великі
#         "lower": input_string.lower(),            # Перетворює всі літери на малі
#         "startswith": input_string.startswith('S'), # Перевіряє, чи починається з "S"
#         "endswith": input_string.endswith('g')    # Перевіряє, чи закінчується на "g"
#     }

import pytest


    # def test_string_methods_operations_upper():
    #     result = string_methods_operations("hello")
    #     assert result["upper"] == "HELLO"  # Перевіряємо, чи правильний результат верхнього регістру

#
# def test_string_methods_operations_lower():
#     result = string_methods_operations("HELLO")
#     assert result["lower"] == "hello"  # Перевіряємо, чи правильний результат нижнього регістру
#
#
# def test_string_methods_operations_startswith_true():
#     result = string_methods_operations("Sample")
#     assert result["startswith"] == True  # Перевіряємо, чи рядок починається з "S"
#
#
# def test_string_methods_operations_startswith_false():
#     result = string_methods_operations("example")
#     assert result["startswith"] == False  # Перевіряємо, чи рядок не починається з "S"
#
#
# def test_string_methods_operations_endswith_true():
#     result = string_methods_operations("running")
#     assert result["endswith"] == True  # Перевіряємо, чи рядок закінчується на "g"
#
#
# def test_string_methods_operations_endswith_false():
#     result = string_methods_operations("run")
#     assert result["endswith"] == False  # Перевіряємо, чи рядок не закінчується на "g"



# Розробіть функцію is_palindrome, яка приймає рядок і повертає True, якщо рядок є паліндромом (читається однаково зліва направо
# і справа наліво) та False в іншому випадку. Напишіть тести для перевірки роботу функції на різних вхідних текстах.
# def is_palindrome(text:str) -> bool:
#     if text == (text, reversed):
#         return True
#
# def test_is_palindrome():
#     assert_that(is_palindrome('rar')).is_true()
#
#

# Словник містить дані про зріст і стать кожної з n=10 осіб. Скласти функцію.,
# яка визначає середній зріст чоловіків. Напишіть тести для перевірки роботу функції на різних вхідних даних.
#
# def avg_height_of_male(dict_in_def) -> float:
#     total_height = 0  # Загальна сума висот чоловіків
#     male_count = 0  # Лічильник чоловіків
#
#     for person in dict_in_def.values():
#         if person['gender'] == 'Male':  # Перевіряємо стать
#             total_height += person['height']  # Додаємо висоту
#             male_count += 1  # Лічимо чоловіків
#
#     # Якщо є чоловіки, обчислюємо середній зріст
#     if male_count > 0:
#         return total_height / male_count
#     else:
#         return 0  # Якщо немає чоловіків, повертаємо 0
#
#
# # Приклад використання
# dictt = {
#     'person1': {'gender': 'Male', 'height': 175},
#     'person2': {'gender': 'Female', 'height': 160},
#     'person3': {'gender': 'Male', 'height': 180},
#     'person4': {'gender': 'Female', 'height': 175},
#     'person5': {'gender': 'Female', 'height': 160},
#     'person6': {'gender': 'Male', 'height': 180},
#     'person7': {'gender': 'Female', 'height': 180},
#     'person8': {'gender': 'Male', 'height': 175},
#     'person9': {'gender': 'Female', 'height': 160},
#     'person10': {'gender': 'Male', 'height': 180},
# }
#
# result = avg_height_of_male(dictt)
# print(result)

# Список містить словники - дані про ціну і тираж кожного з журналів. Скласти програму,
# яка визначає середню вартість журналів, тираж яких більше 10 000 примірників.

# def avg_price_journal(some_list_of_dict):
#     total_price = 0
#     count = 0  # Лічильник елементів, які відповідають умові
#     for x in some_list_of_dict:
#         if x['volume'] >= 10000:
#             total_price += x['price']
#             count += 1
#     if count > 0:
#         return total_price / count  # Повертаємо середню ціну
#     return 0  # Якщо немає елементів з обсягом >= 10000
#
# list_of_dict = [
#     {"name": "Space", "volume": 20000, "price": 12.45},
#     {"name": "SeaSide", "volume": 5000, "price": 10.45},
#     {"name": "Fortune", "volume": 10000, "price": 17.99},
#     {"name": "Vouge", "volume": 25000, "price": 7.68},
# ]
#
# y = avg_price_journal(list_of_dict)
# print(y)

# Скласти функцію, яка повертає тапл де міститься: а) кількість пасажирів, які мають більше двох речей;
# б) чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг;
# в) число пасажирів, кількість речей яких перевершує середнє число речей всіх пасажирів.
#
# list_of_dicts = [
# 	{'number_of_items': 3, 'total_weight': 30},
# 	{'number_of_items': 2, 'total_weight': 20},
# 	{'number_of_items': 1, 'total_weight': 15},
# 	{'number_of_items': 4, 'total_weight': 40},
# 	{'number_of_items': 1, 'total_weight': 10},
# 	{'number_of_items': 1, 'total_weight': 25},
# ]
# def for_all(some_list: list):
# 	sum_of_passangers_with_2_items = 0  # кількість пасажирів, які мають більше двох речей
# 	only_one_item = False  # чи є хоча б один пасажир з однією річчю вагою менше 25 кг
# 	sum_number_of_items = 0  # загальна кількість речей для всіх пасажирів
# 	total_passengers = len(some_list)  # кількість пасажирів
#
# 	for x in some_list:
# 		# а) кількість пасажирів з більше ніж 2 речами
# 		if x['number_of_items'] > 2:
# 			sum_of_passangers_with_2_items += 1
#
# 		# б) чи є хоча б один пасажир з однією річчю вагою менше 25 кг
# 		if x['number_of_items'] == 1 and x['total_weight'] < 25:
# 			only_one_item = True
#
# 		# в) підсумовуємо кількість речей для всіх пасажирів
# 		sum_number_of_items += x['number_of_items']
#
# 	# обчислюємо середнє число речей
# 	average_items = sum_number_of_items / total_passengers if total_passengers > 0 else 0
#
# 	# кількість пасажирів, у яких кількість речей більше середнього
# 	passengers_above_avg = sum(1 for x in some_list if x['number_of_items'] > average_items)
#
# 	# повертаємо результат у вигляді тапла
# 	return (sum_of_passangers_with_2_items, only_one_item, passengers_above_avg)
#
# # Викликаємо функцію та виводимо результат
# fff = for_all(list_of_dicts)
# print(fff)


# Скласти функцію, яка повертає тапл:
# а) прізвище особи, яка має найбільшу зарплату (якщо більше одного - перше по алфавіту);
# б) розмір найменшої зарплати чоловіків, в) розмір найвищої зарплати жінок

# def all_functions(some_dict):
# 	max_salary = 0
# 	lowest_salary_for_man = float('inf')
# 	highest_salary_for_woman = 0
# 	for x in some_dict:
# 		if x['salary'] > max_salary:
# 			max_salary = x['salary']
#
# 		if x['salary'] < lowest_salary_for_man and x['gender'] == 'm':
# 			lowest_salary_for_man = x['salary']
#
# 		if x['salary'] <= max_salary and x['gender'] == 'f':
# 			highest_salary_for_woman = x['salary']
#
# 	last_name_highest_salary = sorted([x['name'] for x in some_dict if x['salary'] == max_salary])[0]
#
# 	return(last_name_highest_salary,lowest_salary_for_man,highest_salary_for_woman)
#
#
# list_of_dicts:list[dict] = [
# 	{"name": "Azimova", "salary": 20000, "gender": "f"},
# 	{"name": "Borenko", "salary": 9000, "gender": "m"},
# 	{"name": "Vasilenko", "salary": 10000, "gender": "m"},
# 	{"name": "Zabolotna", "salary": 25000, "gender": "f"},
# 	{"name": "Koval", "salary": 35000, "gender": "m"},
# 	{"name": "Zaboloteree", "salary": 34000, "gender": "f"},
# 	{"name": "Kovool", "salary": 37000, "gender": "m"},
# ]
#
# y = all_functions(list_of_dicts)
# print(y)

# Скласти функцію, яка визначає середню вартість автомобілів,
# у яких потужність двигуна перевищує 100 к. с.

# def avg_price_of_the_car(some_dict):
#     sum_price_of_all_cars = 0
#     number_of_cars = 0
#     # Проходимо через всі пари (марка, дані про машину) в словнику
#     for car in some_dict.values():
#         # Перевіряємо, чи більше потужність 100 кінських сил
#         if car[0] > 100:
#             sum_price_of_all_cars += car[1]  # Додаємо ціну автомобіля
#             number_of_cars += 1  # Збільшуємо лічильник машин
#
#     if number_of_cars != 0:
#         avg = sum_price_of_all_cars / number_of_cars
#     else:
#         avg = 0
#
#     return avg
#
# dict_of_cars = {
#     "Mersedes": [120, 120000],
#     "Audi": [100, 165000],
#     "VW": [75, 88000],
#     "Toyota": [120, 120000],
#     "Mazda": [110, 170000],
# }
#
# result = avg_price_of_the_car(dict_of_cars)
# print(result)


# Список містить словники - дані співробітників фірми прізвище, вік і відношення до військової служби
# (військовозобов'язаний чи ні). '
#
# Скласти програму, яка визначає:
# а) прізвище наймолодшого за віком співробітника серед військовозобов('язаних (вважати, що такий є і він один); '
# б) прізвища найстарших за віком людей серед військовозобов')язаних і серед невійськовозобов'язаних
# (якщо більше одного - перше по алфавіту)

# def all_functions(some_list_of_dicts):
#     lower_number_of_age = float('inf')
#     surname_person_with_lower_age = str
#     max_number_of_age = 0
#     oldest_military_person = str
#     oldest_not_military_person = str
#     for person in some_list_of_dicts:
#         if person['age']< lower_number_of_age:
#             lower_number_of_age = person['age']
#         if person['age'] == lower_number_of_age and person['military_service'] == True:
#             surname_person_with_lower_age = person['surname']
#         if person['age']> lower_number_of_age and person['military_service'] == True:
#             oldest_military_person = person['surname']
#         if person['age']>lower_number_of_age and person['military_service'] == False:
#             oldest_not_military_person = person['surname']
#
#         if person['military_service']:
#             if (oldest_military_person is None or person['age'] > oldest_military_person[0] or
#                 (person['age'] == oldest_military_person[0] and person['surname'] < oldest_military_person[1])):
#                 oldest_military_person = (person['age'], person['surname'])
#
#         # c) Найстарший серед невійськовозобов'язаних
#         if not person['military_service']:
#             if (oldest_not_military_person is None or person['age'] > oldest_not_military_person[0] or
#                 (person['age'] == oldest_not_military_person[0] and person['surname'] < oldest_not_military_person[1])):
#                 oldest_not_military_person = (person['age'], person['surname'])
#
#     return [lower_number_of_age,surname_person_with_lower_age,oldest_military_person,oldest_not_military_person]
#
# list_of_dicts :list [dict] = [
#     {'surname': 'Heviuk', 'age': 25, 'military_service': True},
#     {'surname': 'Sergenuk', 'age': 31, 'military_service': True},
#     {'surname': 'Dovhanuk', 'age': 31, 'military_service': False},
#     {'surname': 'Susko', 'age': 30, 'military_service': True},
#     {'surname': 'Pelenskiy', 'age': 29, 'military_service': False},
# ]
#
# y = all_functions(list_of_dicts)
# print(y)

# Біометрична авторизація. Функція виконує авторизацію на підставі отриманого списка словників даних та словника,
# отриманого з іншої функції від користувача.
# Параметри користувача: id - int, name - str, second_name - str, age - int
# Якщо дані від користувача співпадають з єталонними даними - користувач отримує повний доступ.
# Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
# Функція повертає рівень доступу: full, read-only, restricted

# def biometric_authorization(database_users, user_input):
#     # Знайдемо користувача за ID
#     for user in database_users:
#         if user['id'] == user_input['id']:
#             # Порівнюємо всі поля
#             matches = sum(1 for key in user if user[key] == user_input[key])
#
#             # Якщо всі поля співпадають - повний доступ
#             if matches == len(user):
#                 return "full"
#             # Якщо співпадає хоча б одне поле - доступ лише для читання
#             elif matches > 0:
#                 return "read-only"
#             # Якщо жодне поле не співпадає - доступ заборонено
#             else:
#                 return "restricted"
#
#     # Якщо користувача з таким ID немає в базі
#     return "restricted"
#
# # Приклади
# database_users = [
#     {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
#     {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
# ]
#
# user_input_1 = {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
# user_input_2 = {"id": 1, "name": "John", "second_name": "Joi", "age": 30}
# user_input_3 = {"id": 1, "name": "John", "second_name": "Joi", "age": 25}
#
# # Тестування
# print(biometric_authorization(database_users, user_input_1))  # full
# print(biometric_authorization(database_users, user_input_2))  # read-only
# print(biometric_authorization(database_users, user_input_3))  # restricted

# Обробка даних з файлової системи (Python-словники)
# Створіть функцію, яка отримує назву файлу та зчитує дані з файлу.
# Програма повинна здійснювати обробку винятку, якщо файл не існує або дані у файлі не є коректним словником Python.
# Завдання функції - визначити кількість елементів у файлі та вивести цю інформацію.
# Застосуйте функцію до декількох файлів та обробіть можливі винятки (FileNotFound, ValueError).
# Приклад використання:

# data1.py = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
# Кількість елементів у файлі data1.py: 2
# ValueError: Файл data2.py містить некоректні дані у форматі Python словників.
# Файл data3.py не знайдено.

# Використовуйте блок try-except для обробки винятків при читанні файлу та зчитуванні даних.
# Використання eval() для отримання значень з файлу та отримання даних у фунцію Python: file_data = eval(file_content, {}),
# Перевірте, чи дані, які ви отримали з файлу, є словником (можливо, з вкладеними структурами даних).
# Обробіть винятки, якщо виникають проблеми при читанні файлу або при перетворенні даних в словник.
import pathlib

# def read_data_and_name(file_to_read):
#     try:
#         # Відкриваємо файл і читаємо його вміст
#         with open(file_to_read, 'r') as file:
#             file_content = file.read()  # Читаємо вміст файлу як рядок
#
#         # Перевіряємо, чи це дійсно рядок
#         if isinstance(file_content, str):
#             # Оцінюємо вміст файлу, перетворюючи його на Python-об'єкт
#             file_data = eval(file_content, {})
#             return file_data
#         else:
#             raise ValueError("File content is not a valid string representation of a list")
#
#     except ValueError as VE:
#         raise Exception(f"Error while processing file content: {VE}")
#     except Exception as e:
#         raise Exception(f"An error occurred: {e}")
#
# # Шлях до файлу
# data1 =  '/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/data1.py'
#
# # Викликаємо функцію з файлом
# result = read_data_and_name(data1)
# print(result)

# До нас наближаються по 2 ворожі кораблі - "sheep1" і "sheep2". Ми знаємо відстань до корабля,
# але наша гармата може влучити тільки в найближчий корабель.
# Написати програму, яка виводитиме назву найближчого корабля, щоб віддати команду на знищення.
# Приклад вхідних даних:

# def first_sheep_to_boom(some_list_of_sheeps):
#     min_length_to_sheep = float('inf')  # Спочатку задаємо дуже велику відстань
#     nearest_sheep = ""  # Змінна для зберігання назви найближчого корабля
#
#     # Проходимо через кожен словник у списку
#     for dict in some_list_of_sheeps:
#         # Знаходимо мінімальну відстань у поточному словнику
#         min_distance_in_dict = min(dict.values())
#
#         # Якщо поточна мінімальна відстань менша за знайдену раніше
#         if min_distance_in_dict < min_length_to_sheep:
#             min_length_to_sheep = min_distance_in_dict
#             # Знаходимо корабель, чия відстань мінімальна
#             nearest_sheep = [key for key, value in dict.items() if value == min_distance_in_dict][0]
#
#     # Повертаємо результат
#     return nearest_sheep
#
#
# result = first_sheep_to_boom(list_of_dicts)
# print(result)  # Виведе: "sheep2"

# Дано рядок, що складається рівно з двох слів, розділених пробілом. Переставте ці слова місцями.
# Результат запишіть у рядок і виведіть отриманий рядок.
# Під час розв'язання цієї задачі НЕ МОЖНА користуватися циклами та інструкцією if.
#
#
# my_string :str = 'Hi Serhii'
# split_string = list(reversed(my_string.split()))
# print(split_string)
# new_string = ' '.join(split_string)
# print(new_string)

# Завдання 1:
#
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

# import csv
#
# def delete_duplicates(first_file, second_file):
#     with open('random.csv', newline='') as csvfile1:
#         reader1 = csv.reader(csvfile1)
#         first_data = [tuple(row) for row in reader1]
#
#     with open('random-michaels.csv', newline='') as csvfile2:
#         reader2 = csv.reader(csvfile2)
#         second_data = [tuple(row) for row in reader2]
#
#     all_data = set(first_data + second_data)
#
#     with open('/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/result_ravliuk.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(all_data)
#
#     return all_data
#
# result = delete_duplicates("/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/random.csv","/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/random-michaels.csv")
# print(result)

#
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і
# повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

# import xml.etree.ElementTree as ET
# import logging
#
# # Налаштування логера
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# def search_by_group_and(some_xml):
#     tree = ET.parse(some_xml)
#     root = tree.getroot()
#
#     # Перебір груп у XML
#     for group in root.findall('group'):
#         group_name = group.find('name')
#         group_number = group.find('number')
#
#         if group_name is not None and group_number is not None:
#             timingExbytes = group.find('timingExbytes')
#             if timingExbytes is not None:
#                 incoming = timingExbytes.find('incoming')
#                 if incoming is not None:
#                     # Логування результату через INFO
#                     logger.info(f"Group {group_name.text}/{group_number.text} has incoming value: {incoming.text}")
#                 else:
#                     logger.info(f"Group {group_name.text}/{group_number.text} doesn't include 'incoming' tag.")
#             else:
#                 logger.info(f"Group {group_name.text}/{group_number.text} doesn't include 'timingExbytes' tag.")
#         else:
#             logger.info("Group with missing 'name' or 'number' found.")
#
#
# # Виклик функції з шляхом до XML-файлу
# result = search_by_group_and("/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/groups (1).xml")
#

# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу
# виведіть через логер на рівні еррор у файл json__<your_second_name>.log
# import logging
# import json
# def valid_json_file(json_file):
#     # logging.basicConfig(filename="json__ravliuk.log",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#     logger = logging.getLogger()
#
#     logging.basicConfig(
#         level=logging.INFO,  # Рівень логування
#         format='%(asctime)s - %(levelname)s - %(message)s',  # Формат виведення
#         handlers=[
#             logging.FileHandler("json__ravliuk.log"),  # Обробник для файлу
#             logging.StreamHandler()  # Обробник для консолі
#         ]
#     )
#
#     try:
#         with open(json_file, 'r') as some_json:
#             json.load(some_json)
#             logger.info(f"json file '{json_file}' is valid json file")
#
#     except json.JSONDecodeError as JD:
#         logger.error(f"file '{json_file}' is not valid json file")
#
# result1 = valid_json_file('/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/localizations_en (1).json')
# result2 = valid_json_file("/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/localizations_ru (1).json")
# result3 = valid_json_file("/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/login (1).json")
# result4 = valid_json_file("/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/swagger (1).json")
#


# Завдання:
# У вас є кілька файлів JSON у папці ideas_for_test/work_with_json.
# Необхідно перевірити, чи всі ці файли є валідними JSON.
# Якщо файл не є валідним, вивести помилку в лог файл json_<your_second_name>.log.
# Логувати всі валідні файли через логер на рівні INFO.
# Вивести в консоль результат для кожного файлу (валідний/невалідний).

# import json
# import logging
# logging.basicConfig(
#             level=logging.INFO,
#             format='%(asctime)s - %(levelname)s - %(message)s',
#             handlers=[
#                 logging.FileHandler("json__ravliuk.log"),
#                 logging.StreamHandler()
#             ]
#         )
# def valid_json_or_no(json_file):
#
#     logger = logging.getLogger()
#
#     try:
#         with open(json_file, 'r') as js:
#             json.load(js)
#             logger.info(f"File '{json_file}' is valid JSON file")
#     except json.JSONDecodeError as JDE:
#         logger.error(f"File '{json_file}' is not valid JSON file")
#
# result1 = valid_json_or_no('/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/localizations_en (1).json')
# result2 = valid_json_or_no("/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/localizations_ru (1).json")
# result3 = valid_json_or_no("/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/login (1).json")
# result4 = valid_json_or_no("/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_5/swagger (1).json")
#

# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об('єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.'
# 'Виведіть інформацію про студента та змініть його середній бал.)

# class Student:
#     first_name : str
#     last_name :str
#     age : int
#     avg_grade : int
#
#     def __init__(self, first_name, last_name, age, avg_grade):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.avg_grade = avg_grade
#
#     def introduction_student(self):
#         return f"Student {self.first_name} {self.last_name} is {self.age} old and his avg grade is {self.avg_grade}"
#
#     def change_student_avg_grade(self, new_avg_grade):
#         self.avg_grade = new_avg_grade
#         return f"Student {self.first_name} {self.last_name} is {self.age} and his changed his avg grade to {self.avg_grade}"
#
# student1 = Student('Andrii', 'Luzan', 34, 172)
# student2 = Student('Valik', 'Mikhienko', 35, 190)
#
# print(student1.introduction_student())
# print(student1.change_student_avg_grade(185))
# print(student1.introduction_student())
#
# class MyClass:
#     def __init__(self, value):
#         self.__private_value = value  # Приватний атрибут
#
#     @property
#     def value(self):
#         """Проперті для отримання значення"""
#         print("Отримуємо значення...")
#         return self.__private_value
#
#     @value.setter
#     def value(self, new_value):
#         """Сеттер для зміни значення"""
#         if new_value < 0:
#             raise ValueError("Значення не може бути від'ємним!")
#         print("Змінюємо значення...")
#         self.__private_value = new_value
#         print(new_value)
#
#
# # Створимо об'єкт
# obj = MyClass(10)
#
# # Отримуємо значення через проперті (не викликаємо метод явно, як звичайний атрибут)
# print(obj.value)  # Викликається метод value(), виведе "Отримуємо значення..."
#
# # Змінюємо значення через сетер
# obj.value = 20  # Викликається метод value.setter(), виведе "Змінюємо значення..."
# print(obj.value)
# # Спробуємо встановити від'ємне значення (викине помилку)
# # obj.value = -5  # ValueError: Значення не може бути від'ємним!
#
# from typing import TypeVar
#
# T = TypeVar('T')  # Створюємо шаблон для типу
#
# def echo(value: T) -> T:
#     return value  # Повертаємо той самий тип, який був переданий
#
# # Викликаємо функцію з різними типами:
# print(echo(10))        # int
# print(echo("hello"))   # str
# print(echo([1, 2, 3])) # list

# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
# значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

# class Romb:
#     def __init__(self, side_a: int, angle_a: int, angle_b: int = None):
#         # Встановлюємо сторону і кути
#         self.side_a = side_a
#         self.angle_a = angle_a
#         if angle_b is not None:
#             self.angle_b = angle_b
#         else:
#             # Якщо не задано angle_b, обчислюємо його як 180 - angle_a
#             self.angle_b = 180 - angle_a
#
#     @property
#     def angle_a(self):
#         return self._angle_a
#
#     @angle_a.setter
#     def angle_a(self, value: int):
#         # Перевірка чи значення кута знаходиться в межах
#         if value <= 0 or value >= 180:
#             raise ValueError("angle_a must be between 0 and 180")
#         self._angle_a = value
#
#     @property
#     def angle_b(self):
#         return self._angle_b
#
#     @angle_b.setter
#     def angle_b(self, value: int):
#         # Перевіряємо, чи сума кутів не перевищує 180
#         if self._angle_a + value != 180:
#             raise ValueError("angle_a + angle_b should be 180")
#         self._angle_b = value
#
# # Тестування:
# def test_romb():
#     romb = Romb(40, 80)  # Створення ромба з заданими значеннями
#     print(f"side_a: {romb.side_a}")
#     print(f"angle_a: {romb.angle_a}")
#     print(f"angle_b: {romb.angle_b}")  # Це автоматично 100, оскільки 180 - 80 = 100
#
#     try:
#         romb.angle_b = 120  # Це викличе ValueError, бо 80 + 120 не дорівнює 180
#     except ValueError as e:
#         print(e)
#
# test_romb()


# Завдання 1
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників.
#Клас TeamLead повинен мати всі атрибути як Manager(ім'я, зарплата, відділ),а також атрибут team_size,який вказує на кількість розробників у команді,якою керує керівник.
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
# class Employee:
#     __name: str
#     __salary: int
#
#     def __init__(self, name: str, salary: int):
#         self.__name = name
#         self.__salary = salary
#
#     @property
#     def get_name(self):
#         return self.__name
#
#     @get_name.setter
#     def set_name(self, value: str):
#         if not isinstance(value, str):
#             raise ValueError(f'Name value:{value} is not string')
#         else:
#             self.__name = value
#
#     @property
#     def get_salary(self):
#         return self.__salary
#
#     @get_salary.setter
#     def set_salary(self, value: int):
#         if not isinstance(value, int):
#             raise ValueError(f'Salary value:{value} is not int')
#         else:
#             self.__salary = value
#
#
# class Manager(Employee):
#     __department: str
#
#     def __init__(self, name: str, salary: int, department: str):
#         super().__init__(name, salary)
#         self.__department = department
#
#     @property
#     def get_department(self):
#         return self.__department
#
#     @get_department.setter
#     def set_department(self, value: str):
#         if not isinstance(value, str):
#             raise ValueError(f"Department value:{value} is not string")
#         else:
#             self.__department = value
#
#
# class Developer(Employee):
#     __programming_language: str
#
#     def __init__(self, name: str, salary: int, programming_language: str):
#         super().__init__(name, salary)
#         self.__programming_language = programming_language
#
#     @property
#     def get_programming_language(self):
#         return self.__programming_language
#
#     @get_programming_language.setter
#     def set_programming_language(self, value: str):
#         if not isinstance(value, str):
#             raise ValueError(f"Programming language value:{value} is not string")
#         else:
#             self.__programming_language = value
#
#
# class TeamLead(Manager, Developer):
#     __team_size: int
#
#     def __init__(self, name: str, salary: int, department: str, team_size: int, programming_language: str = 'Python'):
#         Manager.__init__(self, name, salary, department)  # Викликаємо Manager
#         Developer.__init__(self, name, salary, programming_language)  # Викликаємо Developer
#         self.__team_size = team_size
#
#     @property
#     def get_team_size(self):
#         return self.__team_size
#
#     @get_team_size.setter
#     def set_team_size(self, value: int):
#         if not isinstance(value, int):
#             raise ValueError(f"Team size value:{value} is not int")
#         else:
#             self.__team_size = value
#
# # Тести
# class Tests:
#     def test_including_attributes_manager_and_developer(self):
#         # Тепер тестування працює коректно
#         team_lead = TeamLead(name="Max", salary=5000, department="QA", team_size=5, programming_language="Java")
#         assert team_lead.get_name == "Max"
#         assert team_lead.get_salary == 5000
#         assert team_lead.get_department == "QA"
#         assert team_lead.get_programming_language == "Java"  # Перевіряємо мову програмування
#         assert team_lead.get_team_size == 5
#
#         print("Тест пройдено успішно!")
#
# # Запуск тесту
# test = Tests()
# test.test_including_attributes_manager_and_developer()

# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього декілька (> 2) інших фігур,
# та реалізуйте математично вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
# 
# from abc import ABC, abstractmethod
# class Figure(ABC):
#     def square(self):
#         ...
#     @abstractmethod
#     def parameter(self):
#         ...

import pytest

# class TestExample:
#     def setup_method(self, method):
#         print(f"Налаштування для тесту: {method.__name__}")
#         self.test_data = [1, 2, 3]
#
#     def test_sum(self):
#         assert sum(self.test_data) == 6
#
#     def test_length(self):
#         assert len(self.test_data) == 3







# Є модуль з неоптимальним та помилковим кодом. Ваша задача знайти і виправити помилки у модулі. Хід виконання:
#
# Завантажити репозиторій модулю randominfo.zip
# Скопіювати в папку на свій комп'ютер
# Відкрити папку у новому проекті IDE
# Створити у проекті файл test.py з таким змістом:

import randominfo
person = randominfo.Person()
print(person.full_name, person.gender, person.country, person.address)

# Запустити файл і отримати помилку
# Виправити помилку і запушити у власний бренч у ваш форк
