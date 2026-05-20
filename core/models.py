from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', max_digits=6, decimal_places=2)
    stock = models.IntegerField('In Stock')

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=20)

    def __str__(self):
        return self.name
    
class Sellers(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=20)