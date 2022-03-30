from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Template, Context
from appcoder.forms import *
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

def Viaje(request):
    
    viajes= Viajes.objects.all()
    if request.method == 'POST':
        viaje = ViajesFormulario(request.POST)
        
        if viaje.is_valid():
            data = viaje.cleaned_data
            viaje_nuevo= Viajes(data['destino'],data['pais'],data['anio'])
            viaje_nuevo.save()

        
            return render(request, 'appcoder/blogviajes.html')
            
    else:
        viaje_form = ViajesFormulario()

        return render(request, 'appcoder/blogviajes.html',{'formulario':viaje_form})


def buscarViaje(request):
    
    data = request.GET['destino']                     
   
    print(data)         
    
    if data:
        viaje = Viajes.objects.filter(destino=data) 
         
        return render (request, 'appcoder/buscarViaje.html', {'viaje':viaje[0], "id": data})
        

    return render(request, 'appcoder/buscarViaje.html')