from django.shortcuts import render

def home(request):
    return render(request, 'paginas/home.html')

def catalogo(request):
    return render(request, 'paginas/catalogo.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')        

# Create your views here.
