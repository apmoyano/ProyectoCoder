from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Template, Context


# Create your views here.

def Inicio(request):
    return render(request,'appcoder\index.html')

def Pasajero(request):
    return render(request,'appcoder\pasajero.html')

def Vuelo(request):
    return HttpResponse('Vista Vuelo')

def Aeropuerto(request):
    return HttpResponse('Vista Aeropuerto')

def Equipaje(request):
    return HttpResponse('Vista Equipaje')