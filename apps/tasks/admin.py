from django.contrib import admin

from apps.tasks.models import Contact, Task

# Register your models here.
admin.site.register(Task)
admin.site.register(Contact)
