from django.shortcuts import render
from .models import Product, Clients 

name = 'Victor'

def index(request):
    context = {
        'message': 'Welcome to New York City '+ name +'!',
    }
    return render(request, 'index.html', context)

def contact(request):
    numbers = {
        'phone': '+4199999',
        'email': 'victor@newyorkcity.com'
    }
    return render(request, 'contact.html', numbers)

def about_me(request):
    clients = Clients.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'about_me.html', context)