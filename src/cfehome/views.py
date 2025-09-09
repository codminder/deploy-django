from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

PROJECT_NAME = getattr(settings, "PROJECT_NAME", "Unset Project Name")

def hello_world(request):
    return render(request, "hello-world.html",{
        "project_name": PROJECT_NAME
    })

def health_view(request):
    return HttpResponse("OK")
