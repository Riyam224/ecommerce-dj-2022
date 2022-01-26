from webbrowser import register
from django.contrib import admin

# Register your models here.
from .models import Customer , Product , Cart , CartItems , ShippingAddress


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(ShippingAddress)
