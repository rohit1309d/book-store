from django.contrib import admin
from .models import Book,OrderItem,Order,Payment

# Register your models here.

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)