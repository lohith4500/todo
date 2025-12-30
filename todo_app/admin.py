from django.contrib import admin
from .models import Tasks

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "is_completed", "updated_on")
    search_fields = ("task",)


admin.site.register(Tasks, TaskAdmin)
