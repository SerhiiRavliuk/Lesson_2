# #  Task 1
# proposed_string :str = input("Provide your string here please: ")
#
# unique_counter : int = sum([1 for char in proposed_string if proposed_string.count(char) == 1])
#
# print(unique_counter)
#
# if unique_counter > 10:
#     print(True)
# else:
#     print(False)
#
# #  Task 2
#
# is_correct_srt: bool = False
# while not is_correct_srt:
#     provided_word : str = input("Provide your wordp please: ").lower()
#
#     if provided_word.find("h") != -1:
#         is_correct_srt = True
#
# #  Task 3
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
#
# desired_list : list [str] = [item for item in lst1 if isinstance(item, str)]
#
# print(desired_list)
#
# #  Task 4
#
# provided_list : list[int] = [1,2,3,4,5,6,7,8,9,10]
#
# result : int = sum([integer for integer in provided_list if integer % 2 == 0 ])
#
# print(result)
import logging

# my_iterable = iter("")
#
# # Прохід по ітератору вручну
# print(next(my_iterable))  # Виведе: 1
# print(next(my_iterable))  # Виведе: 2
# print(next(my_iterable))  # Виведе: 3
# print(next(my_iterable))  # Виведе: 4
# print(next(my_iterable))  # Виведе: 5
#
# # Помилка StopIteration при спробі отримати наступний елемент
# try:
#     print(next(my_iterable))
# except StopIteration:
#     print("StopIteration: Ітератор закінчився")

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# def say_hello2():
#     print("Hello2!")
#
# # Приклад з декорування функції за допомогою виклику декоратора
# decorated_function = my_decorator(say_hello2)
# decorated_function()
#
# say_hello()
# say_hello2()

# def validate_params_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Валідація вхідних параметрів
#         for arg in args:
#             if not isinstance(arg, int):  # Перевірка, чи є аргумент цілим числом
#                 raise ValueError(f"Аргумент {arg} має бути цілим числом")
#             if arg < 0:
#                 raise ValueError(f"Аргумент {arg} не може бути від'ємним числом")
#
#         for key, value in kwargs.items():
#             if not isinstance(value, int):  # Перевірка для ключових параметрів
#                 raise ValueError(f"Параметр {key} має бути цілим числом")
#             if value < 0:
#                 raise ValueError(f"Параметр {key} не може бути від'ємним числом")
#
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @validate_params_decorator
# def test_example(param1, param2):
#     # Тут проводяться тести
#     print(f"param1: {param1}, param2: {param2}")
#
# # Виклик функції з коректними параметрами
# test_example(5, 10)  # Має вивести: param1: 5, param2: 10
#
# # Виклик функції з некоректним параметром
# try:
#     test_example(5, -10)  # Має викликати помилку: Аргумент -10 не може бути від'ємним числом
# except ValueError as e:
#     print(f"Помилка: {e}")
#
# # Виклик функції з некоректним типом параметра
# try:
#     test_example("5", 10)  # Має викликати помилку: Аргумент 5 має бути цілим числом
# except ValueError as e:
#     print(f"Помилка: {e}")

# Параметризований декоратор для встановлення максимальної кількості повторних спроб
# def retry(max_retries):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             retries = 0
#             while retries < max_retries:
#                 try:
#                     # Спроба виклику функції, яку декоруємо
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     # Обробка помилки та вивід повідомлення про спробу
#                     print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
#                     retries += 1
#             # Викидаємо виняток, якщо досягнуто максимальну кількість спроб
#             raise Exception("Досягнуто максимальну кількість спроб")
#         return wrapper
#     return decorator
#
# # Параметризоване застосування декоратора
# @retry(max_retries=3)
# def connect_to_server():
#     # Спроба з'єднатися з сервером
#     raise ConnectionError("Не вдалося підключитися до сервера")
#
# # Виклик функції
# connect_to_server()

# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

# class Fibonacci:
#     def __init__(self, number):
#         self.number = number
#         self.current = 0
#
#     def fibonacci_generator(self):
#         a, b = 0, 1
#         while True:
#             yield a
#             a, b = b, a + b
#
#     def pairs_numbers(self):
#         while self.current <= self.number:
#             if self.current % 2 ==0:
#                 yield self.current
#             self.current += 1
#
# fib = Fibonacci(10)
# # Використовуємо генератор для парних чисел
# pairs_gen = fib.pairs_numbers()
#
# # Виведення всіх парних чисел до 10
# for number in pairs_gen:
#     print(number)
#
# # Якщо хочемо використати генератор Фібоначчі
# fib_gen = fib.fibonacci_generator()
#
# # Виведення перших 7 чисел Фібоначчі
# for _ in range(7):
#     print(next(fib_gen))


# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.

# class ReverseIterator:
#     def __init__(self, lst):
#         self.lst = lst  # Зберігаємо список
#         self.index = len(lst) - 1  # Початковий індекс (останній елемент списку)
#
#     def __iter__(self):
#         return self  # Повертаємо сам ітератор
#
#     def __next__(self):
#         if self.index >= 0:
#             result = self.lst[self.index]
#             self.index -= 1
#             return result
#         else:
#             raise StopIteration  # Кидаємо виключення, коли елементи закінчуються
#
# # Приклад використання
# my_list = [1, 2, 3, 4, 5]
# reverse_iter = ReverseIterator(my_list)
#
# for item in reverse_iter:
#     print(item)


# class PairNumbersInIterator:
#     def __init__(self, number):
#         self.number = number  # Це кінцева межа діапазону
#         self.current = 0  # Початкове значення
#
#     def __iter__(self):
#         return self  # Повертаємо сам ітератор
#
#     def __next__(self):
#         # Пропускаємо непарні числа, поки не знайдемо парне
#         while self.current <= self.number:
#             if self.current % 2 == 0:
#                 result = self.current
#                 self.current += 1
#                 return result
#             self.current += 1
#         raise StopIteration  # Кидаємо виключення, коли всі числа в діапазоні будуть перебрані
#
# # Приклад використання:
# pair_number_in_iterator = PairNumbersInIterator(10)  # Всі парні числа до 10
#
# for number in pair_number_in_iterator:
#     print(number)

#
# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.


# import logging
#
# # Налаштування базового конфігурації логування
# logging.basicConfig(
#     filename="logger.log",  # Файл для збереження логів
#     level=logging.INFO,  # Рівень логування
#     format="%(asctime)s - %(levelname)s - %(message)s",  # Формат логів
# )
# logger = logging.getLogger()
#
# # Декоратор для логування аргументів
# def log_arguments(func):
#     def wrapper(self, *args, **kwargs):
#         logger.info(f'We have 2 arguments {args} and {kwargs}')
#         result = func(self, *args, **kwargs)
#         logger.info(f'We got our result and closed the function')
#         return result
#     return wrapper
#
# class LogArguments:
#     a: int = 0
#     b: int = 0
#
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b
#
#     @log_arguments  # Декоратор застосовуємо до методу
#     def sum_of_numbers(self):
#         result = self.a + self.b
#         logger.info(f"Result of adding {self.a} + {self.b} = {result}")
#         return result
#
# # Створення об'єкта класу
# obj = LogArguments(2, 3)
# # Виклик методу через об'єкт
# result = obj.sum_of_numbers()
#
# # Для перевірки результатів у логах, можемо вивести об'єкт
# print(result)


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

# import logging
#
# # Налаштування логування
# logging.basicConfig(
#     level=logging.INFO,  # Рівень логування
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     handlers=[
#         # logging.StreamHandler(),  # Логування в консоль
#         logging.FileHandler("logger.log")  # Логування у файл
#     ]
# )
# logger = logging.getLogger()
# def catch_exceptions(func):
#     def wrapper(*args, **kwargs):
#         # Логування аргументів
#         logger.info(f"We have 2 arguments {args}")
#
#         # Перевірка, чи є усі аргументи числами (int або float)
#         try:
#             for arg in args:
#                 if not isinstance(arg, (int, float)):  # Перевірка на int чи float
#                     raise ValueError(f"Argument {arg} is not a number")
#             # Якщо всі аргументи правильні, викликаємо функцію
#             result = func(*args, **kwargs)
#             return result
#         except ValueError as e:
#             logger.error(f"Some of the arguments {args} is not a valid number: {e}")
#             print(f"Error: {e}")
#             return None  # Повертаємо None або інше значення на випадок помилки
#         finally:
#             logger.info(f"We completed calculation in our func")
#
#     return wrapper
#
# # Приклад використання декоратора
#
# @catch_exceptions
# def add_numbers(a, b):
#     return a + b
#
# # Викликаємо функцію з правильними аргументами
# result = add_numbers(2, 34)
# print(f"Result: {result}")
#
# # Викликаємо функцію з неправильними аргументами
# result = add_numbers(2, 'three')
# print(f"Result: {result}")



# Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото
# зробленi ровером “Curiosity” на Марсi.
# Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою
# додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg .
# Завдання потрiбно зробити використовуючи модуль requests

# Початковi данi

# import requests
#
# BASE_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
# MARS_PHOTO_1_URL = 'mars_photo1.jpg'
# MARS_PHOTO_2_URL = 'mars_photo2.jpg'
# params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
#
#
# response = requests.get(BASE_URL,params=params)
# print(response.json())
#
# if response.status_code == 200:
#     data = response.json()
#     if 'photos'in data:
#         photos = data['photos']



import flask

# Сервер стартує за базовою адресою http://127.0.0.1:8080
# Враховуючи документацiю яку наведено нижче вам потрiбно написати код який використовуючи
# модуль request зробить через POST upload якогось зображення на сервер,
# за допомогою GET отримає посилання на цей файл и потiм за допомогою DELETE зробить видалення файлу з сервера
# Документацiя для app.py
# Cерверна частина надає можливість завантажувати, отримувати та видаляти зображення.
# Завантаження зображення
# Метод: POST
#
# Шлях: /upload
#
# Опис: Завантажує зображення на сервер.
#
# Параметри запиту:
#
# image: файл зображення (тип MIME: image/*)
# Відповідь:
#
# Код стану 201 (Created) у разі успішного завантаження.
# Повертає URL завантаженого зображення у форматі JSON:
# Copy code
# {
#     "image_url": "<http://127.0.0.1:8080/uploads/example.jpg>"
# }
# Отримання URL завантаженого зображення
# Метод: GET
#
# Шлях: /image/<filename>
#
# Опис: Повертає URL або саме зображення в залежності від заголовка Content-Type. **<filename>** повинен бути вказаним враховуючи правила кодування ULR
#
# Відповідь:
#
# Код стану 200 (OK)
# Повертає URL завантаженого зображення у форматі JSON, якщо Content-Type рівний text:
# Copy code
# {
#     "image_url": "<http://127.0.0.1:8080/uploads/example.jpg>"
# }
# Повертає саме зображення, якщо Content-Type рівний image.
# Видалення зображення
# Copy code
# jsonCopy code
# {
#     "message": "Image example.jpg перейменовано на new_example.jpg"
# }
#
# Метод: DELETE
#
# Шлях: /delete/<filename>
#
# Опис: Видаляє завантажене зображення з серверу. **<filename>** повинен бути вказаним враховуючи правила кодування ULR
#
# Відповідь:
#
# Код стану 200 (OK) у разі успішного видалення.
# Повертає повідомлення про успішне видалення у форматі JSON:
# Copy code
# {
#
#     "image_url": "http://127.0.0.1:8080/uploads/example.jpg"
#
# }

