import unittest
# from unittest.mock import MagicMock, patch, Mock
from profiles.func_to_test import toIncreaseText, factorial

# my_mock_func = MagicMock(return_value=1)

class TestSimple(unittest.TestCase):
    def test_to_upper_case(self):
        data_in = 'some_text'
        expected_data = data_in.upper()
        actual_result = toIncreaseText(data_in)
        self.assertEqual(actual_result, expected_data)


# class TestMock(unittest.TestCase):
#     @patch('profiles.func_to_test', my_mock_func)
#     def test_factorial(self):
#         self.assertEqual(factorial(5), 120)