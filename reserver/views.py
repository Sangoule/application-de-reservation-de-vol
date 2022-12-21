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
    return render(request,'vols/acceuils_vols.html',context)
def compagnies(request):
    compagnies=Compagnie.objects.all()
    context={'compagnies':compagnies}
    return render(request,'compagnies/accueil_cie.html',context)
def volsdetails(request,pk):
    vols=Vols.objects.gets(id=pk)
    context={'vols':vols}
    return render(request,'vols/accueil_cie.html',context)


