from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)

    
class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre

class IngredienteEnHamburguesa(models.Model):
    hamburguesa_id = models.ForeignKey('Hamburguesa', on_delete=models.CASCADE)
    ingrediente_id = models.ForeignKey('Ingrediente', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hamburguesa_id) + ',' + str(self.ingrediente_id)