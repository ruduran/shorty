from unittest.mock import patch
from datetime import datetime

from django.test import TestCase

from shortener.utils import generate_and_get_url_code, DEFAULT_CODE_LENGTH


class CodeGenerationTests(TestCase):
    @patch('shortener.utils.datetime')
    def test_different_code_because_of_time(self, datetime_mock):
        url = 'url'
        datetime_mock.now.return_value = datetime(2018, 7, 13, 10, 30, 0, 0)
        first_code = generate_and_get_url_code(url)
        datetime_mock.now.return_value = datetime(2018, 7, 13, 10, 30, 0, 1)
        second_code = generate_and_get_url_code(url)

        self.assertNotEqual(first_code, second_code)
        self.assertEqual(DEFAULT_CODE_LENGTH, len(first_code))
        self.assertEqual(DEFAULT_CODE_LENGTH, len(second_code))

    @patch('shortener.utils.datetime')
    def test_code_collision_just_uses_one_more_char(self, datetime_mock):
        url = 'url'
        datetime_mock.now.return_value = datetime(2018, 7, 13, 10, 30, 0, 0)
        first_code = generate_and_get_url_code(url)
        second_code = generate_and_get_url_code(url)

        self.assertNotEqual(first_code, second_code)
        self.assertEqual(DEFAULT_CODE_LENGTH, len(first_code))
        self.assertEqual(DEFAULT_CODE_LENGTH + 1, len(second_code))
