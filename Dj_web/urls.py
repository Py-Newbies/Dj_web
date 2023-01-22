from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("emp.urls")),
    path("students/", include("students.urls")),
]
