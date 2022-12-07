from django import forms

class ConyugueFormulario(forms.Form):
    
    nombre= forms.CharField()
    tipo_de_pariente= forms.CharField()
    email=forms.EmailField()
    
    
class FamiliarFormulario(forms.Form):
    nombre= forms.CharField(min_length=3, max_length=50)
    edad= forms.IntegerField()

    
