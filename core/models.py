from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', max_digits=6, decimal_places=2)
    stock = models.ImageField('In Stock')

class Clients(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=20)
    
class Sellers(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=20)