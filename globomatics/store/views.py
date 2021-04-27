from django.shortcuts import render
from django.http import  HttpResponse , HttpResponseNotFound


# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


def index(request):
    return HttpResponse("Hellllo ")


def detail(request):
    return HttpResponse("Hello there globomatics is an ecommerce  store for all thingdselectronic")

@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def electronics(request):
    if request.method == "GET":
        print(request.headers)
        print("-----------------/n", request)
        return HttpResponse("THis is the Made in Kenya Electronics section")
    if request.method == 'POST':
        print("This is not allowed")
        return HttpResponseNotFound("This is not allowed")

