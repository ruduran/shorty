import hashlib
import base64
from datetime import datetime

from django.db import IntegrityError, transaction

from .models import ShortenedUrl


DEFAULT_CODE_LENGTH = 3


def generate_and_get_url_code(url):
    now = datetime.now()
    str_to_hash = '{}{}'.format(url, now.isoformat())
    digest = hashlib.sha1(str_to_hash.encode()).digest()
    code = base64.b64encode(digest)

    saved = False
    length = DEFAULT_CODE_LENGTH
    while not saved:
        try:
            short_url = ShortenedUrl(url=url, code=code[:length].decode().replace('/', '_'))
            with transaction.atomic():
                short_url.save()
            saved = True
        except IntegrityError:
            length += 1

    return short_url.code
