from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),

]
