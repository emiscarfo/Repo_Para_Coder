from django.urls import path
from appEmi.views import *

urlpatterns = [
    path("inicio/", inicio, name="apli-emi-inicio"),
    path("nombres/", nombres, name="apli-emi-nombres"),
    path("gradofamilia", gradofamilia, name="apli-emi-familiar"),
    path("edades/", edades,name="apli-emi-edades"),
    path("emails/", emails, name="apli-emi-emails"),
    #path("fechanacimientos/", fechanacimientos),
           
]




