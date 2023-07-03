from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login



def home(request):
    return render(request, 'core/index.html ')

def login(request):
    return render(request, 'core/login.html')


def registrar(request):
    return render(request, 'core/registrar.html')

def about(request):
    return render(request, 'core/about.html')


