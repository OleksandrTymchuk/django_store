from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import UserSignUpForm, UserSignInForm
from .models import MenuItem
from products.models import Product


def home(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(display_on_main_page=True, approved = True).order_by("id")
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


def add_to_cart(request, product_id):
    if Product.objects.get(id=product_id):
        if product_id in request.session.get("products", []):
            return redirect("/")
        if request.session.get("products", False):
            request.session["products"].append(product_id)
            request.session.modified = True
        else:
            request.session["products"] = []
            request.session["products"].append(product_id)
    else:
        raise Http404()
    return redirect("/")


def cart(request):
    if request.session.get("products", False):
        products = Product.objects.filter(id__in=request.session.get("products"))
        return render(request, "main/cart.html", {"products": products})
    else:
        return render(request, "main/cart.html", {})


def remove_from_cart(request, product_id):
    if request.session.get("products", False):
        for i in range(len(request.session.get("products"))):
            if request.session.get("products")[i] == product_id:
                del request.session.get("products")[i]
                request.session.modified = True
    return redirect("/cart")