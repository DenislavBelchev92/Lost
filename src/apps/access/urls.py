from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'access'
urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
