from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def shop(request):
    return render(request, 'main/shop.html')


def single(request):
    return render(request, 'main/single-product.html')


def cart(request):
    return render(request, 'main/cart.html')


def checkout(request):
    return render(request, 'main/checkout.html')
