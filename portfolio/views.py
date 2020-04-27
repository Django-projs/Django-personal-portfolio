from django.shortcuts import render
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all()     # all objects from Project module is fetched from database and returns to our view page
    return render(request, 'portfolio/home.html', {'projects':projects})
