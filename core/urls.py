from  django.urls import path

from .views import index, contact, about_me, who_am_i

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('about_me/', about_me,),
    path('about_me/<int:pk>', who_am_i, name='who_am_i')
]