from django.shortcuts import render
import json
import requests


# Create your views here.


def index(request):

    return render(request, 'frontend/index.html')

def about(request):
    
    return render(request, 'frontend/about.html')

def contact(request):
    
    return render(request, 'frontend/reservation.html')