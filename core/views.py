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

def who_am_i(request, pk):
    clients = Clients.objects.get(id=pk)
    context={
        'clients':clients
    }
    print(f'Here is the PK: {pk}')
    print(f'Here is your name: {clients.phone}')
    return render(request, 'who_am_i.html', context)