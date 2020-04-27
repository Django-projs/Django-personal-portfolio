from django.contrib import admin
from .models import Project

# Register your models here.
# Create Models what we want to show up inside the admin page

admin.site.register(Project)
# The database admin page takes us to the next page where a new module is created with the name project, hwere you can add your projects.

