from django.http import HttpResponse
from django.shortcuts import render
from ticketing.models import Ticket
import random
import string


def randomstring(stringlength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringlength))


def index(request):
    return render(request, 'index.html')


def submit(request):
    # new_ticket = Ticket(submitter= randomstring(), body='Help m e with this bug')
    # new_ticket.save()
    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        new_ticket = Ticket(submitter=username, body=body)
        new_ticket.save()
        return HttpResponse ("Successfully submitted ticket")
    return render(request, 'submit.html')


    return render(request, 'submit.html')


def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets': all_tickets})


