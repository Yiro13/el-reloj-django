from django.db import models

# Create your models here.
class Project(models.Model):
    nombre = models.CharField(max_length = 200)
    correo = models.CharField(max_length = 200)
    pregunta = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)