from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks

# Create your views here.


def addTask(request):
    task = request.POST["task"]
    Tasks.objects.create(task=task)
    return redirect("home")


def updateTask(request):
    pass


def deleteTask(request):
    pass
