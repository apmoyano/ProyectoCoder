from pyexpat import model
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Template, Context
from appcoder.models import *

#vista basadas en clases

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView

class ViajeLista(ListView):

    model = Viajes
    template_name = 'appcoder/viajes_list.html'

class ViajeDetalle(DetailView):

    model = Viajes
    template_name = 'appcoder/viajes_detalle.html'

class CrearViaje(CreateView):
    model = Viajes
    success_url ='/appcoder/viajes/list'
    fields = ['destino','pais','año'] 

class UpdateViaje(UpdateView):
    model = Viajes
    success_url ='/appcoder/viajes/list'
    fields = ['destino'] 

class DeleteViaje(DeleteView):
    model = Viajes
    success_url ='/appcoder/viajes/list'
     


# Create your views here.

def Inicio(request):
    return render(request,'appcoder/index.html')

def Viajes(request):
    return render(request,'appcoder/blogpost.html')

def Comidas(request):
    return HttpResponse('Vista Comida')

def Montanas(request):
    return HttpResponse('Vista Montanas')


def Formulario(request):
    return render(request, 'appcoder/formularios.html')