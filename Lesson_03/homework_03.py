alice_in_wonderland = "\nWould you tell me, please, which way I ought to go from here?\n""That depends a good deal on where you want to get to, said the Cat.\n" "I don't much care where — said Alice.\n" "Then it doesn't matter which way you go, said the Cat.\n" "—— so long as I get somewhere, Alice added as an explanation.\n" "Oh, you're sure to do that, said the Cat, "  "if you only walk long enough."
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_see = 436402
azov_see = 37800
total_area = black_see + azov_see
print("\nЗагальна площа Чорного та Азовсьокого морів становить", total_area, "км2.\n")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_number = 375291
first_and_second = 250449
second_and_third = 222950
third_storage = total_number - first_and_second
first_storage = total_number - second_and_third
second_storage = total_number - first_storage -third_storage
print("Кількість товарів а першому складі -",first_storage,"товарів.\nНа другому складі - ",second_storage,"товарів.\nНа третьому складі - ",third_storage,"товарів.\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = 18
monthly_payment = 1179
computer_cost = monthly_payment * months
print("Вартість комп'ютера становить",computer_cost,"грн.\n")

# task 07

"Остача від діленя чисел:"
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("a =",a,"; \nb =",b,"; \nc =",c,"; \nd =",d,"; \ne =",e,"; \nf =",f,";\n")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274
small_pizza = 218
juice = 35
cake = 350
water = 21
sum_of_money = (big_pizza * 4)+(small_pizza*2)+(juice*4)+cake+(water*3)
print("Іринці знадобиться",sum_of_money,"грн.\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
photos_on_page = 8
pages_need = all_photos / photos_on_page
print("Ігору знадобиться",pages_need,"сторінок\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
litres_per_100 = 9
full_cistern = 48
sum_of_litres = total_distance / litres_per_100
print("Для такої подорожі знадобиться",sum_of_litres,"літрів бензину.")
number_of_petrol = sum_of_litres / full_cistern
print("Необхідно буде заїхати на заправку щонайменше",int(number_of_petrol),"рази.")