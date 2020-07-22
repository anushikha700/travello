from django.urls import path

from testapp import views

urlpatterns = [
    path('', views.hello_world,name='hello_world'),
    path('add', views.add, name='add'),


]
