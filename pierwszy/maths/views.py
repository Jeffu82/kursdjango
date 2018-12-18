from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def operacje(request, operacja, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    if operacja =="add":
        wynik = arg1 + arg2
    elif operacja =="sub":
        wynik = arg1 - arg2
    elif operacja == "div":
        if arg2 == 0:
            wynik = "nie dziel przez zero"
        else:
            wynik = arg1 / arg1


    return HttpResponse(wynik)

