from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Tasks


def home(request):
    in_complete_tasks = Tasks.objects.filter(is_completed=False).order_by("-created_on")
    print(in_complete_tasks)
    context = {"in_complete_tasks": in_complete_tasks}
    return render(request, "home.html", context)
