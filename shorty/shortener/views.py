from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import ShortenedUrl
from .utils import generate_and_get_url_code


def index(request):
    context = {}
    if request.POST.get('url'):
        url = request.POST['url']
        code = generate_and_get_url_code(url)

        path = reverse('redirection', args=[code])

        context['url'] = request.POST['url']
        context['short_url'] = "http://{}{}".format(request.get_host(), path)

    return render(request, 'shortener/index.html', context)


def redirection(request, code):
    shortened = get_object_or_404(ShortenedUrl, code=code)
    return HttpResponseRedirect(shortened.url)
