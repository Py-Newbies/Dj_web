from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('connect', views.connect, name='connect'),
    path('signup/', views.create_customer, name='create_customer'),
]
