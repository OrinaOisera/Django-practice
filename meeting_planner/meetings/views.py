from django.shortcuts import render
from .models import Meeting

# Create your views here.


def detail(request, id):
    meeting = Meeting.objects.geet(pk=id)
    return render(request, "meetings/detail.html", {"meetings": meeting})
