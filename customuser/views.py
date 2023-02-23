from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from . import models


def home(request):
    return render(request, "home.html")


def connect(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            page_path = request.user.department  # this cane be leads/ or staff/ etc
            return render(request, f'{page_path}/dashboard.html')
    return render(request, 'login.html')


def create_customer(request):
    if request.method == 'POST':
        first_name = request.POST['Name']
        email = request.POST['email']
        department = request.POST['department']
        password = request.POST['password']
        hashed_password = make_password(password)
        customer = models.CustomUser(email=email, first_name=first_name,
                                     department=department, password=hashed_password)
        customer.save()
        return redirect('home')
    return render(request, 'createUser.html')


def logout_view(request):
    logout(request)
    return redirect('home')