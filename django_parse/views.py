from django.shortcuts import render
import datetime


def home(request):
    date=datetime.datetime.now().date()
    name = 'Dave'
    _context = { 'name': name,
                 'date' : date,
                }
    return render(request, 'home.html',_context)