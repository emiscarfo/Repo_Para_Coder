from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre= models.CharField(max_length=50)
    tipo_de_pariente= models.CharField(max_length=25)
    edad= models.IntegerField()
    email= models.EmailField()
    fecha_nac= models.DateField()






