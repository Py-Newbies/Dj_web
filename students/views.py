from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    username = request.GET.get('name')
    password = request.GET.get('token')
    user = authenticate(username=username, password=password)
    print(username, password, request.user, '#' * 20, user is not None)
    # http://127.0.0.1:8000/students/login/?name=reddy&token=5FvSJ4QChnV_G.C
    if user:
        login(request, user)
        return redirect('student_details')
    return HttpResponse("Login failed")


def details(request):
    print(request.user)
    return render(request, "home.html")
