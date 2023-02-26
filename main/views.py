from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignUpForm, UserSignInForm
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
    form = UserSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get("password"))
        user = form.save()
        login(request, user)
        return redirect("/")
    return render(request, "main/sign-up.html", {"form": form})

def sign_in(request):
    form = UserSignInForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            request.session["invalid_user"] = True
    return render(request, "main/sign-in.html", {"form": form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")