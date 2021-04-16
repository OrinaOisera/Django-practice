from django.shortcuts import render , get_list_or_404
from .models import Meeting

# Create your views here.


def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    # meeting = get_list_or_404(Meeting)
    return render(request, "meetings/detail.html", {"meeting": meeting})
