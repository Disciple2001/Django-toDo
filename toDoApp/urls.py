from django.urls import path

from toDoApp import views

urlpatterns = [
    path('', views.home, name='home'),

    # Todo urls
    path('todo/addTask', views.addTask, name='addTask'),
    path('todo/mark_as_done/<int:pk>', views.mark_as_done, name='mark_as_done'),
    path('todo/mark_as_undone/<int:pk>', views.mark_as_undone, name='mark_as_undone'),
    path('todo/editTask/<int:pk>', views.editTask, name='editTask'),
    path('todo/deleteTask/<int:pk>', views.deleteTask, name='deleteTask')

]
