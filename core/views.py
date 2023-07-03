from django.shortcuts import render
from django.contrib.auth.views import logout_then_login
# Create your views here.

def home(request):
    return render(request, 'core/index.html ')

def login(request):
    return render(request, 'core/login.html')


