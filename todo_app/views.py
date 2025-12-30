from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tasks

# Create your views here.


def addTask(request):
    task = request.POST["task"]
    Tasks.objects.create(task=task)
    return redirect("home")


def mark_as_done(request, pk):
    # task = Tasks.objects.update().
    task = get_object_or_404(Tasks, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("home")


def mark_as_undone(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.is_completed = False
    task.save()
    return redirect("home")


def edit_todo_task(request, pk):
    # print(request.POST)
    old_task = get_object_or_404(Tasks, pk=pk)
    if request.method == "POST":
        get_updated_task = request.POST["task"]
        old_task.task = get_updated_task
        print("get_updated_task", get_updated_task)
        old_task.save()
        return redirect("home")
    else:
        context = {"old_task": old_task}
        print("context", context)
        return render(request, "edit_todo_task.html", context)


def deleteTask(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect("home")
