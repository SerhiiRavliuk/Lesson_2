import unittest
from homework_9 import sum_of_numbers
from homework_9 import cheack_str
from homework_9 import check_number_divisible_by_2
from homework_9 import max_letters
from homework_9 import list_of_words
from homework_9 import get_word_with_h

class My_first_tests(unittest.TestCase):

    def test_sum_positive_of_numbers(self):
        expected_result = 9
        result = sum_of_numbers(4,5)
        self.assertEqual(result, expected_result)

    def test_sum_negative_of_numbers(self):
        expected_result = 9
        result = sum_of_numbers(-3, 4)
        self.assertNotEqual(result, expected_result, msg=f'The test failed. The result {result} is not equal to the expected result.')

    def test_positive_is_str(self):
        some_str = 'Slavik'
        result = cheack_str(some_str)
        self.assertTrue(result, f'{result} is string')

    def test_negative_is_str(self):
        some_str = 3.5
        result = cheack_str(some_str)
        self.assertTrue(not result, msg= f'{result} is not string')

    def test_positive_divisible_by_2(self):
        result = check_number_divisible_by_2(8)
        self.assertTrue(result, f'{result} is not divisible by 2')

    def test_negative_divisible_by_2(self):
        result = check_number_divisible_by_2(5)
        self.assertTrue(not result, f'{result} is not divisible by 2')

    def test_max_letters(self):
        result = max_letters(list_of_words)
        self.assertEqual(result, "Margarita", msg=f'The test failed. The result {result} is not equal to the expected result.')

    def test_negative_max_letters(self):
        result = max_letters(list_of_words)
        self.assertNotEqual(result, "Andrii", msg=f'The test failed. The result {result} is equal to the expected result.')

    def test_word_with_h(self):
        result = get_word_with_h('hello')
        self.assertTrue(result, msg=f'Our string {result} is include letter "h".')

    def test_word_with_h_after_invalid_inputs(self):
        result = get_word_with_h('elllo')
        self.assertTrue(not result, msg=f'Our string {result} is not include letter "h".')

if __name__ == '__main__':
    unittest.main()


