from django.shortcuts import render
from .models import Almohadon
from .forms import AlmohadonForm 

def home(request):
    return render(request, 'paginas/home.html')

def catalogo(request):
    return render(request, 'paginas/catalogo.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')  

def productos(request):
    almohadones = Almohadon.objects.all()
    return render(request, 'productos/index.html', {'productos': almohadones})   

def crear(request):
    formulario = AlmohadonForm(request.POST or None)
    return render(request, 'productos/crear.html', {'formulario': formulario})       

def editar(request):
    return render(request, 'productos/editar.html')         

# Create your views here.
