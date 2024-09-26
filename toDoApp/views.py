from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from toDoApp import models


# Create your views here.

def home(request):
    tasks = models.Task.objects.filter(status=1).order_by('-created_at')
    completed_tasks = models.Task.objects.filter(status=2).order_by('-created_at')

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)


def addTask(request):
    task = request.POST['task']
    models.Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, pk):
    # task = models.Task.objects.filter(pk=pk)
    # task.update(status=2)

    task = get_object_or_404(models.Task, pk=pk)
    task.status = 2
    task.save()

    return redirect('home')


def mark_as_undone(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    task.status = 1
    task.save()
    return redirect('home')


def editTask(request, pk):
    get_task = get_object_or_404(models.Task, pk=pk)
    if request.method == 'POST':
        task_name = request.POST['task']
        get_task.task = task_name
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)


def deleteTask(request, pk):
    task = get_object_or_404(models.Task, pk=pk)
    task.delete()
    return redirect('home')
