from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def welcome(request):
    return HttpResponse("Welcome to parade ")


def date(request):
    return HttpResponse("This request was made on: " + str(datetime.now()))


def about(request):
    return HttpResponse("This is SBC's  parade and assembly schedule")
