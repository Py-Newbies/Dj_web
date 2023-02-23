from django.http import HttpResponse
from django.shortcuts import render
from . import models


def validate_user(name, token):
    try:
        user = models.Student.objects.get(name=name, token=token)
        return user
    except models.Student.DoesNotExist:
        return False


def details(request):
    username = request.GET.get('name')
    password = request.GET.get('token')
    user = validate_user(username, password)
    if user:
        return render(request, "students/update.html", {'student': user})
        # return render(request, 'home.html')
    else:
        return HttpResponse("kindly login before proceeding further")


def create(request):
    if request.method == "POST":
        name = "-".join(request.POST.get("name").split())
        number = request.POST.get("num")
        user = models.Student(name=name, mobile_num=number, created_by=request.user)
        user.save()
        # fixme this is temporary only
        url = f"http://127.0.0.1:4040/students/details?name={user.name}&token={user.token}"
        return HttpResponse(url)
    else:
        return render(request, "students/create_user.html")


def dashboard(request):
    return render(request, "students/dashboard.html")

