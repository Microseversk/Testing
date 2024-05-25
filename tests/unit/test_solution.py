import unittest
from unittest import TestCase
from solution import Solution



class TestSolution(TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_palindromic_substrings_count__correct_result(self):
        data = [['abc', 3], ['aaa', 6], ['aaabccc',13],['asdasd',6],['ytreeeeqweeeeerrreee',45]]
        for s in data:
            with self.subTest(string=s[0], right_count=s[1]):
                self.assertEqual(self.sol.countSubstrings(s[0]), s[1])

    def test_palindromic_substrings_count__incorrect_result(self):
        data = [['abca', 3], ['abcb', 3]]
        for s in data:
            with self.subTest(string=s[0], wrong_count=s[1]):
                self.assertNotEqual(self.sol.countSubstrings(s[0]), s[1])

    def test_palindromic_substrings_count__input_string_length_valid(self):
        min_input_string_length = 1
        max_input_string_length = 1000
        data = {
            "left_on_bound": "a",
            "left_gt_bound": "aa",
            "right_on_bound": "a" * max_input_string_length,
            "right_lt_bound": "a" * (max_input_string_length - min_input_string_length),
        }
        #Сделал так потому что в логике проверки можем поломать проверочные значения и на корректные входные данные вылетит ex
        for s in data:
            with self.subTest(input_string_type=s, input_string_length=len(data[s])):
                try:
                    self.sol.countSubstrings(data[s])
                except Exception as e:
                    self.fail(e)

    def test_palindromic_substrings_count__input_string_length_invalid(self):
        min_input_string_length = 1
        max_input_string_length = 1000
        data = {
            "left_lt_bound": "",
            "right_gt_bound": "a" * (max_input_string_length + min_input_string_length),
        }
        for s in data:
            with self.subTest(input_string_type=s, input_string_length=len(data[s])):
                self.assertRaises(AssertionError, self.sol.countSubstrings, data[s])

    def test_palindromic_substrings_count__input_string_type_invalid(self):
        data = [
            123,
            12.3,
            ['a', 'b', 'c'],
            {'a': 1, 'b': 2},
            None
        ]
        for s in data:
            with self.subTest(input_string_type=type(s)):
                self.assertRaises(TypeError, self.sol.countSubstrings, s)

    def test_palindromic_substrings_count__input_string_value_invalid(self):
        data = [
            '123',
            "123abc123",
            "abc123abc",
            'ABC',
            "abcABC",
            "abcABCabc",
            "ABCabcABC",
            "абц",
            "абцabcабц",
            "abcабцabc",
            '異體字',
            "異體字abc異體字",
            "abc異體字abc",
            " ",
            "abc ",
            " abc",
            "abc abc",
            "@#!",
            "!@#abc!@#",
            "abc!@#abc"
        ]
        for s in data:
            with self.subTest(incorrect_input_value=s):
                self.assertRaises(AssertionError, self.sol.countSubstrings, s)



if __name__ == '__main__':
    unittest.main()