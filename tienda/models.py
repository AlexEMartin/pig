from django.db import models

# Create your models here.
class Almohadon(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True)

    def __str__(self):
        fila = 'Título: ' + self.titulo + ' - ' + 'Descripción: ' + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    

class Funda(models.Model):
    id=models.AutoField(primary_key=True)
    coleccion=models.CharField(max_length=100, verbose_name='Colección')
    modelo=models.CharField(max_length=100, verbose_name='Modelo')
    tamano=models.CharField(max_length=8, verbose_name='Tamaño')
    imagen_funda = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    
    def __str__(self):
        fila = 'Colección: ' + self.coleccion + ' - ' + 'Modelo: ' + self.modelo
        return fila
    
    