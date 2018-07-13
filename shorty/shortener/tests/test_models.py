from django.test import TestCase

from shortener.models import ShortenedUrl


class ShortenedUrlTests(TestCase):

    def test_str(self):
        code = 'code'
        url = ShortenedUrl(url='url', code=code)
        self.assertEqual(code, str(url))
