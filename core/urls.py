from  django.urls import path

from .views import index, contact, about_me

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('about_me/', about_me),
]