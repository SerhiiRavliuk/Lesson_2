# task_1

def multiplication_table(number):
    multiplier = 1

    while multiplier * number:
        result = number * multiplier

        if result > 25:

            break
        else:print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def calculated(first_figure : int, second_figure : int):

    result : int = first_figure + second_figure
    print('\nСума двох чисел = ', result)
calculated(3,6)
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
list_figures: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def average(numbers: list[int]) -> float:
    total_sum = sum(numbers)
    count = len(numbers)
    return total_sum / count

result = average(list_figures)
print(result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
our_string :str = input("Напишіть рядок, який потрібно повернути у зворотньому напрямку: ")
def reversed_input(input_string):
    return (input_string[::-1])

result = reversed_input(our_string)
print(result)


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def max_letters(word: list[str]):
    return max(word, key = len)

list_of_words: list[str] = ["Serhii", "Stepan", "Max", "Margarita"]

result = max_letters(list_of_words)
print(result)
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))



def unique_symbols_count(symbols: str) -> int:
    unique_symbols = []
    symbols = symbols.lower()

    for char in symbols:
        if char not in unique_symbols:
            unique_symbols.append(char)

    return len(unique_symbols)
def more_than_10(count: int) -> bool:
    return count > 10

string_input = input("Введіть символи: ")

unique_count = unique_symbols_count(string_input)
print(f"Кількість унікальних символів: {unique_count}")

print(more_than_10(unique_count))

# task 8

list_numbers: list[int] = [1,2,3,4,5,6,9,12]
sum_of_numbers = list([pairs for pairs in list_numbers if pairs % 2 == 0])

print(sum(sum_of_numbers))



lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 : list[str] = ([strings for strings in lst1 if isinstance(strings, str)])
print(lst2)



car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)

def find_matching_cars(car_data, criteria):
  year_min, engine_min, price_max = criteria

  return sorted(
    (car for car, details in car_data.items()
     if details[1] >= year_min and details[2] >= engine_min and details[4] <= price_max),
    key=lambda car: car_data[car][4]
  )[:5]

result = find_matching_cars(car_data, search_criteria)

for car in result:
  print(f"{car}: {car_data[car]}")
