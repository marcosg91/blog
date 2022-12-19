from django.shortcuts import render
from Articulos.models import Entrada
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.conf import include
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
    return render(request, "bienvenida.html", {"articulos":articulos})

def  register(request):
    if request.method == "POST":
        form=UserCreationForm (request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            messages.success(request, f"usuario{username}creado ")
    else:
        form=UserCreationForm()
    context={"form": form}
    
    return render (request, "social/register.html",context)

def Quienes_somos(request):
    return render (request, "social/Quienes_somos.html")

def Noticias(request):
    return render (request, "Noticias.html")

def login(request):
    return render (request, "registration/login.html")

@login_required
def inicio1(request):
    return HttpResponse("HOLA")
