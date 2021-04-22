from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hellllo ")


def detail(request):
    return HttpResponse("Hello there globomatics is an ecommerce  store for all thingdselectronic")
