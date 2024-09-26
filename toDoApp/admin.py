from django.contrib import admin

from toDoApp import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'status', 'updated_at')
    search_fields = ('task',)


# Register your models here.

admin.site.register(models.Task, TaskAdmin)
