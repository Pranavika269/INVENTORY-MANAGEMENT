from django.contrib import admin

# Register your models here.
# inventory/admin.py
from .models import Category, Product, Supplier

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
