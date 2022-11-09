from django.shortcuts import render, redirect
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
    formulario = AlmohadonForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html', {'formulario': formulario})       

def editar(request, id):
    almohadon = Almohadon.objects.get(id=id)
    formulario = AlmohadonForm(request.POST or None, request.FILES or None, instance=almohadon)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/editar.html', {'formulario': formulario})  

def eliminar(request, id):
    almohadon = Almohadon.objects.get(id=id)
    almohadon.delete()
    return redirect('productos')           

# Create your views here.
