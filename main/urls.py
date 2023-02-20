from django.urls import path
from .views import home, sign_up, sign_in, logout_view

urlpatterns = [
    path("", home, name="home"),
    path("sign-up", sign_up, name="sign-up"),
    path("sign-in", sign_in, name="sign-in"),
    path("logout", logout_view, name="logout")

]
