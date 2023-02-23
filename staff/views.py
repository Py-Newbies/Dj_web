from django.shortcuts import render


def dashboard(request):
    return render(request, "staff/dashboard.html")


def create(request):
    return render(request, "staff/create.html")