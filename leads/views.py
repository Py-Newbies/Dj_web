from django.shortcuts import render


def dashboard(request):
    return render(request, "leads/dashboard.html")


def create(request):
    return render(request, "leads/create.html")
