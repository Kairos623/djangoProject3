from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    return render(request, 'main/index.html')


def shop(request):
    product = Product.objects.all()
    return render(request, 'main/shop.html', {'Product': product})


def single(request):
    return render(request, 'main/single-product.html')


def cart(request):
    return render(request, 'main/cart.html')


def checkout(request):
    return render(request, 'main/checkout.html')
