from django.urls import re_path

from . import views

urlpatterns = [
    re_path('(?P<code>[0-9a-zA-Z\+_]+)', views.redirection, name='redirection'),
    re_path('', views.index, name='index'),
]
