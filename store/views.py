from math import prod
from django.shortcuts import render

# Create your views here.
from .models import Product , Cartitems , Cart 


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart , created  = Cart.objects.get_or_create(customer=customer , completed=False)
        cartitems = cart.cartitems_set.all()
        
    products = Product.objects.all()

    context = {
        'products': products,
        'cart': cart
    }
    return render(request , 'store.html' , context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart , created  = Cart.objects.get_or_create(customer=customer , completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}

    context = {
        'cartitems' : cartitems, 'cart':cart
    }
    return render(request , 'cart.html', context)


def checkout(request):
    pass