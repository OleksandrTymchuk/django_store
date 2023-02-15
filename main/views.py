from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem
from products.models import Product

def home(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(display_on_main_page=True, approved = True).order_by("id")
    return render(request, 'main/index.html', {
        "menu_items": menu_items,
        "products":products
    })
