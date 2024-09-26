from django.http import HttpResponse
from django.shortcuts import render

from toDoApp import models


# Create your views here.

def home(request):
    tasks = models.Task.objects.filter(status=1).order_by('-created_at')
    context = {
        'tasks': tasks
    }
    return render(request, 'home.html', context)


def addTask(request):
    task = request.POST['task']
    models.Task.objects.create(task=task)
    return HttpResponse('Form submitted')
