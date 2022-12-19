from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from reserver.models import *
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def vols(request):
    vols=Vol.objects.all()
    context={'vols':vols}
    return render(request,'vols.html',context)


