from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the VloGo's index.")
def ee(request):
    return HttpResponse("You encountered an easter eggs")
