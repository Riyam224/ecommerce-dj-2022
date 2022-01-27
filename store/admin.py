from django.contrib import admin

# Register your models here.
from .models import Customer , Product , Cart , Cartitems , ShippingAddress



admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(ShippingAddress)
