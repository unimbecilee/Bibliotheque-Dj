from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *

def home(request):
    return render(request, "index.html",context={"current_tab": "home"})

def home(request):
    return render(request, "home.html",context={"current_tab": "home"})

def lecteur(request):
    return render(request, "lecteur.html",context={"current_tab": "lecteur"})

def livres(request):
    return render(request, "livres.html",context={"current_tab": "livres"})

def casier(request):
    return render(request, "casier.html",context={"current_tab": "casier"})

def rendus(request):
    return render(request, "rendus.html",context={"current_tab": "rendus"})

def shopping(request):
    return HttpResponse("Bienvenue sur la page de shopping")

def lecteur_tab(request):
    lecteur = lecteur.objects.all()
    return render(request,"lecteur.html",
                                context={"current_tab":"lecteur", 
                                        "lecteur": lecteur})
