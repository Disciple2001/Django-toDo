from django.urls import path

from toDoApp import views

urlpatterns = [
    path('', views.home, name='home')
]