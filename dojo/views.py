# dojo/views.py

from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    # request: HttpRequest

    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)