from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/index.html ')

def login(request):
    return render(request, 'core/login.html ')

def registro(request):
    return render(request, 'core/registro.html ')