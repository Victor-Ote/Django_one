from  django.urls import path
from .views import index, contact, about_me, who_am_i, error_404
from django.conf import urls

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('about_me/', about_me,),
    path('about_me/<str:name>', who_am_i, name='who_am_i')
]

urls.handler404 = error_404