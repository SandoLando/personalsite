from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse


def IndexView(request):
    return render(request, 'home/index.html')

def ResumeView(request):
    return render(request, 'home/resume.html')

def ProjectsView(request):
    return render(request,'home/projects.html')
        
    

