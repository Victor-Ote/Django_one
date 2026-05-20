from django.contrib import admin
from .models import Product, Clients, Sellers

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Clients, ClientsAdmin)