from django.shortcuts import render, get_object_or_404
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

def who_am_i(request, name):
    result_name = name[0].upper() + name[1:]
    # clients = Clients.objects.get(name=f'{result_name}')
    clients = get_object_or_404(Clients, name=f'{result_name}')
    
    context = {
        'clients': clients
    }
    return render(request, 'who_am_i.html', context)

def error_404(request, exception):
    return render(request, '404.html', status=404)

