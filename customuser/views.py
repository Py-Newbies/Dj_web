from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")

@csrf_exempt
def connect(request):
    if request.method == 'POST':
        # as per the department, use should be able to see the dashboard
        page_path = '' # this cane be leads/ or staff/ etc
        # as of now it is pointing towards super admin dashbord
        return render(request, f'{page_path}dashboard.html')

    return render(request, "login.html")