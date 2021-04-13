from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def welcome(request):
    return render(request, "website/welcome.html", {"message": "THis data was sent from the view to the template"})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse(" NAME: Mark Orina Town: Eldoret   County : ug")
