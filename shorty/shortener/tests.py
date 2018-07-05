from django.test import TestCase
from django.urls import reverse

from .models import ShortenedUrl


class ShortenedUrlTests(TestCase):

    def test_str(self):
        code = 'code'
        url = ShortenedUrl(url='url', code=code)
        self.assertEqual(code, str(url))


class RedirectTests(TestCase):

    valid_url = None

    def setUp(self):
        self.valid_url = ShortenedUrl(url='url', code='code')
        self.valid_url.save()

    def tearDown(self):
        if self.valid_url is not None:
            self.valid_url.delete()

    def test_valid_redirection(self):
        response = self.client.get(reverse('redirection', args=[self.valid_url.code]))
        self.assertEqual(response.status_code, 302)
        self.assertIn(response.url, self.valid_url.url)

    def test_invalid_redirection(self):
        response = self.client.get(reverse('redirection', args=['not_valid']))
        self.assertEqual(response.status_code, 404)
