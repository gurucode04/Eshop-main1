from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

from django.contrib.auth.models import Group

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class AdminOrders(admin.ModelAdmin):
    list_display = ('product','customer')

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order,AdminOrders)

admin.site.unregister(Group)


# username = Tanushree, email = tanushree7252@gmail.com, password = 1234
