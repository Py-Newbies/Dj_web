from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, ),
    path('create/', views.create, name='create')
]
