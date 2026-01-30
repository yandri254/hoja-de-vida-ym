from django.contrib import admin
from .models import DatosPersonales, FormacionAcademica, ExperienciaLaboral, ReferenciaPersonal

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'email', 'telefono')

@admin.register(FormacionAcademica)
class FormacionAcademicaAdmin(admin.ModelAdmin):
    list_display = ('nivel', 'institucion', 'estado')

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'fecha_inicio', 'fecha_fin')

@admin.register(ReferenciaPersonal)
class ReferenciaPersonalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email')