from django.shortcuts import render
from .models import Product, Clients 

def index(request):
    context = {
        'message': 'Welcome to New York City '+ Clients.name +'!',
    }
    return render(request, 'index.html', context)

def contact(request):
    numbers = {
        'phone': '+4199999',
        'email': 'victor@newyorkcity.com'
    }
    return render(request, 'contact.html', numbers)