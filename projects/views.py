from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projects_list = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "A full-stack ecommerce platform with product listings, cart, and payment integration.",
    },
    {
        "id": "2",
        "title": "Blog Application",
        "description": "A blogging platform with user authentication, post creation, and commenting features.",
    },
    {
        "id": "3",
        "title": "Task Management System",
        "description": "A productivity app to create, assign, and track tasks with deadlines and status updates.",
    },
    {
        "id": "4",
        "title": "Real-time Chat App",
        "description": "A web-based chat application using WebSockets for real-time messaging.",
    },
    {
        "id": "5",
        "title": "Portfolio Website",
        "description": "A personal portfolio website to showcase projects, skills, and contact information.",
    },
]


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {"project": project_obj})
