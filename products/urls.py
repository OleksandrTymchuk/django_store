from django.urls import path
from .views import add_product,\
    product_details,\
    add_category,\
    category_page,\
    update_product

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/update/<int:id>", update_product, name="update_product"),
    path("/category/add", add_category, name="add_category"),
    path("/<int:id>", product_details, name="product_details"),
    path("/category/<str:slug>", category_page, name="category_page"),

]