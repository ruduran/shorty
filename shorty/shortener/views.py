from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import ShortenedUrl
from .utils import generate_and_get_url_code


def validate(url):
    if '://' not in url:
        return "You need to enter the protocol. For instance http://{}".format(url)
    else:
        return ""


def index(request):
    context = {}
    if request.POST.get('url'):
        url = request.POST['url']
        context['url'] = url

        validation_error = validate(url)
        if validation_error:
            context['error'] = validation_error
        else:
            code = generate_and_get_url_code(url)
            path = reverse('redirection', args=[code])
            context['short_url'] = "http://{}{}".format(request.get_host(), path)

    return render(request, 'shortener/index.html', context)


def redirection(request, code):
    shortened = get_object_or_404(ShortenedUrl, code=code)
    return HttpResponseRedirect(shortened.url)
