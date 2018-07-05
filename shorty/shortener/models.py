from django.db import models


class ShortenedUrl(models.Model):
    url = models.TextField()
    code = models.CharField(max_length=32, unique=True, db_index=True)

    def __str__(self):
        return self.code
