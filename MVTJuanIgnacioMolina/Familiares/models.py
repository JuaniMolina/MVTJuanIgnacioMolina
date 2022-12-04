from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    descripcion = models.TextField()
    nacimiento = models.DateField()

    def __str__(self):
        return 'Nombre: ' + self.nombre + ' Apellido: ' + self.apellido + ' Nacimiento :' + str(self.nacimiento) + ' Descripcion: ' + self.descripcion