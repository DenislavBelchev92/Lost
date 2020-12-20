from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'profile_page'
urlpatterns = [
    path('', views.index, name='index'),
]