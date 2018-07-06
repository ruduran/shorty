import hashlib
import base64

from .models import ShortenedUrl


def generate_and_get_url_code(url):
    digest = hashlib.sha1(url.encode()).digest()
    code = base64.b64encode(digest)
    short_url = ShortenedUrl(url=url, code=code[:3].decode())
    short_url.save()
    return short_url.code
