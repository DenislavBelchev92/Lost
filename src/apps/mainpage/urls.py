from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

]
