from django.db import models

# Create your models here.

class Familiar(models.Model):
     nombre= models.CharField(max_length=50)
     edad= models.IntegerField()
     
     def __str__(self):
           return f"Nombre: {self.nombre} --> Edad: {self.edad}"
         

class Conyugues(models.Model):
     nombre= models.CharField(max_length=50)
     tipo_de_pariente= models.CharField(max_length=25)
     email= models.EmailField()    
     def __str__(self):
           return f"Nombre: {self.nombre.upper()}, {self.tipo_de_pariente.capitalize()},  [{self.email.title()}]"
     #fecha_nac= models.DateField()

