from django.contrib import admin

# Register your models here.
from .models import Hamburguesa, Ingrediente, IngredienteEnHamburguesa

admin.site.register(Hamburguesa)
admin.site.register(Ingrediente)
admin.site.register(IngredienteEnHamburguesa)
