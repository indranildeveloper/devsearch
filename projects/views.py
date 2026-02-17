from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {"project": project_obj})


def create_project(request):
    form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/project_form.html", context)
