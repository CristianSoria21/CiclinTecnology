from django.contrib import admin
from posiciones.models import Categoria, Competidor, Equipo, Carrera, Organizador, OrgCarr, CarrEqui, CompCat
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Competidor)
admin.site.register(Equipo)
admin.site.register(Carrera)
admin.site.register(Organizador)
admin.site.register(OrgCarr)
admin.site.register(CarrEqui)
admin.site.register(CompCat)
