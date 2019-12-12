# from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Home, Description

# Create your views here.

# Index Page
def home(request):
    return render(request, 'live_app/home.html', {})

def description(request):
    return render(request, 'live_app/description.html', {})

def ulang(request, home_id):
    homes = Home.objects.get(pk=home_id)
    return render(request, 'home.html', {'homes':homes})
