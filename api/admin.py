from django.contrib import admin
from .models import Category,Product,Customer

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)