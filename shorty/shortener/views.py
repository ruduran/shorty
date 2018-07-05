from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import ShortenedUrl


def redirection(request, code):
    shortened = get_object_or_404(ShortenedUrl, code=code)
    return HttpResponseRedirect(shortened.url)
