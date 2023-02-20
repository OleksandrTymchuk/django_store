from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuItem
from django.contrib.auth.models import User
from products.models import Product

def home(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(display_on_main_page=True, approved = True).order_by("id")
    print(request.user)
    return render(request, 'main/index.html', {
        "menu_items": menu_items,
        "products":products
    })

def sign_up(request):
    if request.method == "POST":
        user = User()
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.set_password(request.POST.get("password"))
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        if user:
            login(request, user)
        return redirect("/")

    else:
        return render(request, "main/sign-up.html", {})

def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        print("AUTH")
        print(user)
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign-in.html", {})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")