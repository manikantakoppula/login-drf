from django.urls import path
from django.contrib import admin
from .views import register,user_login,user_logout
app_name = 'accounts'
urlpatterns = [
     path('register/',register,name='register'),
     path('',user_login,name='login'),
     path('logout/',user_logout,name='logout'),
     ]