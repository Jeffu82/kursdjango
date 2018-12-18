from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

from .models import Wpis


# Create your views here.


def index(request):
    wpisy = Wpis.objects.all()
    wynik = ""
    for w in wpisy:
        wynik += f"<li>{w.tytul}</li>"

    wynik = f"<ul>{wynik}</ul>"
    return HttpResponse(wynik)


def index_temp(request):
    ostatni_wpis = Wpis.objects.last()
    liczby = [x for x in range(10)]
    context = {
        'chleb': '1,90',
        'woda': '1,60',
        'wpis': ostatni_wpis,
        'liczby': liczby
    }
    return render(
        request=request,
        template_name='blog/index.html',
        context=context
    )