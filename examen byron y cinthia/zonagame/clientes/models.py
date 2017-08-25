from django.db import models

class cliente(models.Model):
    nombre=models.CharField(max_length=50,help_text='Ingrese el nombre del cliente: ')
    telefono=models.CharField(max_length=10,help_text='Ingrese el numero de telefono: ')
    sexo=models.CharField(max_length=1,help_text='Ingrese el sexo: ')
    fecha=models.DateField(help_text='Ingrese la fecha de nacimiento: ')
