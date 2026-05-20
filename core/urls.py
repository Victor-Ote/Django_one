from  django.urls import path

from .views import index, contact, about_me, who_am_i

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('about_me/', about_me,),
    path('who_am_i/<int:pk>', about_me, name='who_am_i')
]