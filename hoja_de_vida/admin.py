from django.contrib import admin

from .models import (
    DatosPersonales,
    ExperienciaLaboral,
    FormacionAcademica,
    ReferenciaPersonal,
)

admin.site.register(DatosPersonales)
admin.site.register(FormacionAcademica)
admin.site.register(ExperienciaLaboral)
admin.site.register(ReferenciaPersonal)
