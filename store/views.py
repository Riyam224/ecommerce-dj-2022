from math import prod
from this import d
from django.http import JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from .models import Product , Cartitems , Cart 


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart , created  = Cart.objects.get_or_create(customer=customer , completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}
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
    return render(request, 'checkout.html', context = {})



def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
    cartitem, created = Cartitems.objects.get_or_create(cart = cart, product = product)

    if action == "add":
        cartitem.quantity += 1
        cartitem.save()
    

    return JsonResponse("Cart Updated", safe = False)



def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = Cartitems.objects.filter(product__name = quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Quantity updated", safe = False)
