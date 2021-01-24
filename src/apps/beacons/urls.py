from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'beacons'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('details/id=<int:id>', views.add, name='details'),

]