from what_is_year_now import what_is_year_now
import unittest
from unittest.mock import patch


class TestWhatIsYearNow(unittest.TestCase):
    def test1(self):
        exp_year = what_is_year_now()
        self.assertEqual(exp_year, 2023)

    def test2(self):
        self.assertRaises(TypeError, what_is_year_now, 42)

    def test3(self):
        with patch('what_is_year_now.json.load') as mocked_datetime_dict:
            test_dict = {'currentDateTime': '01.03.2019'}
            mocked_datetime_dict.return_value = test_dict
            self.assertEqual(what_is_year_now(), 2019)
            mocked_datetime_dict.assert_called_once()

    def test4(self):
        with patch('what_is_year_now.json.load') as mocked_datetime_dict:
            test_dict = {'currentDateTime': '42123415'}
            mocked_datetime_dict.return_value = test_dict
            self.assertRaises(ValueError, what_is_year_now)
            mocked_datetime_dict.assert_called_once()
