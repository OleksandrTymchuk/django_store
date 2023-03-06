from django.urls import path
from .views import \
    home,\
    sign_up,\
    sign_in,\
    logout_view,\
    add_to_cart,\
    cart,\
    remove_from_cart

urlpatterns = [
    path("", home, name="home"),
    path("sign-up", sign_up, name="sign-up"),
    path("sign-in", sign_in, name="sign-in"),
    path("logout", logout_view, name="logout"),
    path("add-to-cart/<int:product_id>", add_to_cart, name="add_to_cart"),
    path("cart", cart, name="cart"),
    path("remove-from-cart<int:product_id>", remove_from_cart, name="remove-from-cart"),

]
