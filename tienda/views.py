from django.shortcuts import render, redirect
from .models import Almohadon
from .forms import AlmohadonForm, CustomerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    almohadones = Almohadon.objects.all()
    return render(request, 'paginas/home.html', {'productos': almohadones})


def catalogo(request):
    return render(request, 'paginas/catalogo.html')


def contacto(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'paginas/contacto.html', {'form': form})


@login_required
def productos(request):
    almohadones = Almohadon.objects.all()
    return render(request, 'productos/index.html', {'productos': almohadones})

@login_required
def crear(request):
    formulario = AlmohadonForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html', {'formulario': formulario})

@login_required
def editar(request, id):
    almohadon = Almohadon.objects.get(id=id)
    formulario = AlmohadonForm(
        request.POST or None, request.FILES or None, instance=almohadon)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/editar.html', {'formulario': formulario})

@login_required
def eliminar(request, id):
    almohadon = Almohadon.objects.get(id=id)
    almohadon.delete()
    return redirect('productos')

@login_required
def salir(request):
    logout(request)
    return redirect('/')

# Create your views here.
