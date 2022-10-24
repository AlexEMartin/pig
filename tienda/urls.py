from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('contacto', views.contacto, name='contacto'),
    path('productos', views.productos, name='productos'),
    path('productos/crear', views.crear, name='crear'),
    path('productos/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('productos/editar/<int:id>', views.editar, name='editar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)