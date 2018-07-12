import hashlib
import base64
import datetime

from django.db.utils import IntegrityError

from .models import ShortenedUrl


def generate_and_get_url_code(url):
    now = datetime.datetime.now()
    str_to_hash = '{}{}'.format(url, now.isoformat())
    digest = hashlib.sha1(str_to_hash.encode()).digest()
    code = base64.b64encode(digest)

    saved = False
    length = 3
    while not saved:
        try:
            short_url = ShortenedUrl(url=url, code=code[:length].decode().replace('/', '_'))
            short_url.save()
            saved = True
        except IntegrityError:
            length += 1

    return short_url.code
