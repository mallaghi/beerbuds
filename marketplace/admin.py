from django.contrib import admin
from .models import Store, Profile, Beer, Order, OrderItem, Cart, CartItem

# Register your models here.

admin.site.register(Store)
admin.site.register(Profile)
admin.site.register(Beer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)

