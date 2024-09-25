from django.http import HttpResponse
from django.shortcuts import render

from toDoApp import models


# Create your views here.

def home(request):
    tasks = models.Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context)
