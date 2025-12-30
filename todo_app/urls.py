from django.urls import path
from . import views

urlpatterns = [
    path("addTask/", views.addTask, name="addTask"),
    path("updateTask/", views.updateTask, name="updateTask"),
    path("deleteTask/", views.deleteTask, name="deleteTask"),
]
