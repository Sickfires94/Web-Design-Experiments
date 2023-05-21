from django.urls import path

from . import views

urlpatterns = [
path('', views.blank, name="home"),
path('home', views.home, name="home")

    ]