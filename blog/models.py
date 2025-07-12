from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    link = models.URLField(blank=True)
    fecha = models.DateField()

class EntradaBlog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)

class SobreMi(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    
class Certificado(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='certificados/')


