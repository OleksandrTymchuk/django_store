from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm

def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            categories = Category.objects.order_by("-id")
            form = ProductForm(initial={
                "user":request.user
            })
            return render(request, "products/add.html", {"form":form, "categories":categories})
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(user=request.user)
                if request.POST.getlist("categories", False):
                    for category_id in request.POST.getlist("categories"):
                        category = Category.objects.get(id=category_id)
                        category.products.add(product)
                return redirect("/")
            else:
                return render(request, "products/add.html", {"form": form})
    else:
        return redirect("/")

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product":product})

def add_category(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            if request.POST.get("title"):
                category = Category()
                category.user = request.user
                category.title = request.POST.get("title")
                category.parent_id = int(request.POST.get("parent_category"))
                category.save()
                return redirect("/")
        else:
            categories = Category.objects.order_by("-id")
            return render(request, "products/category/add.html", {"categories":categories})
