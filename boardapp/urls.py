from django.contrib import admin
from django.urls import path, include
from .views import signupfunc, loginfnc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc

urlpatterns = [
    path("signup/", signupfunc, name='signup'),
    path('login/', loginfnc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read')
]
