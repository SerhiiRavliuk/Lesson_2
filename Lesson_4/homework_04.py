adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart.And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

replace_string = adwentures_of_tom_sawer.replace("\n", "")
print(replace_string)

# task 02 ==
""" Замініть .... на пробіл
"""
withot_drots = adwentures_of_tom_sawer.replace("...." , " ")
print(withot_drots)
print("\n")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами\n.
"""

one_space_text = print(withot_drots.replace("  "," "))
print("\n")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
lower_cases = adwentures_of_tom_sawer.lower()
print(lower_cases.count("h"))
print("\n")
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

import re
print(len(re.findall(r'[A-Z]',adwentures_of_tom_sawer)))
print("\n")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_Tom = adwentures_of_tom_sawer.find("Tom")
second_Tom = adwentures_of_tom_sawer.find("Tom",first_Tom + 1)
print(f"{second_Tom}")
print("\n")
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
split_by_end = withot_drots.split(".")
print(split_by_end)
print("\n")
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

four_line = lower_cases[431:536]
print(four_line)
print("\n")
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print(adwentures_of_tom_sawer.count("By the time"))
print("\n")
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentents_words = len("And when the middle of the afternoon came, from being a \
poor poverty, stricken boy in the morning, Tom was literally \
rolling in wealth.".split())
print(last_sentents_words)