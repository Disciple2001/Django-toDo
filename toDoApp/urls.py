from django.urls import path

from toDoApp import views

urlpatterns = [
    path('', views.home, name='home'),

    # Todo urls
    path('todo/addTask', views.addTask, name='addTask')

]
