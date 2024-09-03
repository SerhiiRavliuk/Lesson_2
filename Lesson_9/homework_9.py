"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_numbers(first_number,second_number):
    return first_number+second_number

def max_letters(word: list[str]):
    return max(word, key = len)

list_of_words: list[str] = ["Serhii", "Stepan", "Max", "Margarita"]

def cheack_that_is_str(some_str : str):
        if isinstance(some_str) is str:
            return True
def get_number_that_is_divisible_by_2(element) :
    if element % 2 ==0:
        return True

def get_word_with_h(word: str) -> str:

    word_lower = word.lower()

    if 'h' in word_lower:
        return word
    else:
        raise ValueError('No "h" character found in word')