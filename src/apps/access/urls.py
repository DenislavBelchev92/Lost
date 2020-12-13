from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'access'
urlpatterns = [
    path('', views.loginView, name='login'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
]
