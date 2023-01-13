from django.shortcuts import render


def home(request):
    return render(request, "dashboard.html")


def login(request):
    return render(request, "signin.html")


def signup(request):
    return render(request, "signup.html")
