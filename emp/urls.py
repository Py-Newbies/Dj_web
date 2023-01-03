from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("Login", views.login),
    path("Signup", views.signup)
]