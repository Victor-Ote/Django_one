from django.shortcuts import render

def index(request):
    context = {
        'message': 'Welcome to New York City!',
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')