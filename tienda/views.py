from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('<h1>Bienvenide a la Tienda</h1>')

# Create your views here.
