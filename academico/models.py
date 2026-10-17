from django.db import models

# Create your models here.
class Programa(models.Model):
    nombre_programa = models.CharField(max_length=120)
    nivel = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_programa
    
     