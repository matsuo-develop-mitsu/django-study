from django.contrib import admin
from django.urls import path, include
from .views import signupfunc, loginfnc, listfunc
urlpatterns = [
    path("signup/", signupfunc, name='signup'),
    path('login/', loginfnc, name='login'),
    path('list/', listfunc, name='list')
]
