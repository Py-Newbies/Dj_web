from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create, name=''),
    path("details", views.details, name='student_details'),
]
