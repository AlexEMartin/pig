from django.shortcuts import render

def home(request):
    return render(request, 'paginas/home.html')

def catalogo(request):
    return render(request, 'paginas/catalogo.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')  

def productos(request):
    return render(request, 'productos/index.html')   

def crear(request):
    return render(request, 'productos/crear.html')       

def editar(request):
    return render(request, 'productos/editar.html')         

# Create your views here.
