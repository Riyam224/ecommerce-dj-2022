import uuid
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import uuid


class Customer(models.Model):
    user =  models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name



class Product(models.Model):
    name =  models.CharField(_("name"), max_length=50)
    price = models.FloatField(_("price"))
    image = models.ImageField(_("image"), upload_to='product/')

    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(Customer, verbose_name=_("customer"), related_name='cart_customer', on_delete=models.CASCADE)
    cart_id = models.UUIDField(_("cart id") , default=uuid.uuid4 , unique=True , editable=False)
    completed = models.BooleanField(_("completed") , default=False)
    

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return str(self.cart_id)



class CartItems(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_("cart"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity") , default=0)

    

    class Meta:
        verbose_name = _("CartItems")
        verbose_name_plural = _("CartItemss")

    def __str__(self):
        return str(self.product.name)



class ShippingAddress(models.Model):
    customer =  models.ForeignKey(User, verbose_name=_("customer"), on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name=_("cart"), on_delete=models.CASCADE)
    address = models.CharField(_("address"), max_length=250)
    city = models.CharField(_("city"), max_length=250)
    state = models.CharField(_("state"), max_length=250)
    zipcode = models.CharField(_("zipcode"), max_length=250)

    

    class Meta:
        verbose_name = _("ShippingAdress")
        verbose_name_plural = _("ShippingAdresss")

    def __str__(self):
        return str(self.address)
