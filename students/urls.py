from django.urls import path
from . import views

urlpatterns = [
    path("", views.details, name='student_details'),
    path("login/", views.login_view, name='login'),
]
