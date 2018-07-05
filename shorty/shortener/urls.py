from django.urls import re_path

from . import views

urlpatterns = [
    re_path('(?P<code>[0-9a-zA-Z]+)', views.redirection, name='redirection'),
]
