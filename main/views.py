from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem

def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'main/index.html', {"menu_items": menu_items})
