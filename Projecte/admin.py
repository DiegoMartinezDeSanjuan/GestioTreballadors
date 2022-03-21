from django.contrib import admin

# Register your models here.
from Projecte.models import Project, Worker

admin.site.register(Project)
admin.site.register(Worker)
