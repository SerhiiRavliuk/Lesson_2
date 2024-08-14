# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести
# “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний ввід буде - 10, 60, “Не можу це зробити”.

my_list = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
def sum_of_parts(s):
    try:
        parts = s.split(',')
        result = [int(element) for element in parts]
        return sum(result)

    except ValueError as excepted:
        return "Не можу це зробити!"

for item in my_list:
    print(sum_of_parts(item))