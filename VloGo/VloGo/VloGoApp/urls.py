from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ee/", views.ee, name="Easter Egg"),
]