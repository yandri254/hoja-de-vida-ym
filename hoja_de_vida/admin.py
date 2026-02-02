from django.contrib import admin

from .models import (
    DatosPersonales,
    ExperienciaLaboral,
    FormacionAcademica,
    ReferenciaPersonal,
    Reconocimiento,
    CursoRealizado,
    ProductoAcademico,
    ProductoLaboral,
    VentaGarage,
)


@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'numero_cedula', 'perfil_activo']
    list_filter = ['perfil_activo', 'sexo', 'estado_civil']
    search_fields = ['nombres', 'apellidos', 'numero_cedula']
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombres', 'apellidos', 'numero_cedula', 'sexo', 'estado_civil', 
                      'nacionalidad', 'lugar_nacimiento', 'fecha_nacimiento', 'licencia_conducir', 'imagen')
        }),
        ('Contacto', {
            'fields': ('telefono_convencional', 'telefono_fijo', 'email', 'sitio_web',
                      'direccion_domiciliaria', 'direccion_trabajo')
        }),
        ('Perfil Profesional', {
            'fields': ('descripcion_perfil', 'titulo_profesional', 'perfil', 'perfil_activo')
        }),
        ('Visibilidad de Secciones', {
            'fields': ('mostrar_perfil', 'mostrar_experiencia', 'mostrar_formacion', 
                      'mostrar_referencias', 'mostrar_reconocimientos', 'mostrar_cursos',
                      'mostrar_productos_academicos', 'mostrar_productos_laborales', 'mostrar_venta_garage'),
            'classes': ('collapse',)
        }),
    )


@admin.register(FormacionAcademica)
class FormacionAcademicaAdmin(admin.ModelAdmin):
    list_display = ['nivel', 'institucion', 'estado', 'activo']
    list_filter = ['estado', 'activo']
    search_fields = ['nivel', 'institucion', 'titulo']


@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ['cargo_desempenado', 'nombre_empresa', 'fecha_inicio_gestion', 'fecha_fin_gestion', 'activo']
    list_filter = ['activo', 'nombre_empresa']
    search_fields = ['cargo_desempenado', 'nombre_empresa', 'descripcion_funciones']
    ordering = ['-fecha_inicio_gestion']


@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ['tipo_reconocimiento', 'descripcion_reconocimiento', 'entidad_patrocinadora', 'fecha_reconocimiento', 'activo']
    list_filter = ['tipo_reconocimiento', 'activo']
    search_fields = ['descripcion_reconocimiento', 'entidad_patrocinadora']


@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    list_display = ['nombre_curso', 'entidad_patrocinadora', 'total_horas', 'fecha_inicio', 'fecha_fin', 'activo']
    list_filter = ['activo', 'entidad_patrocinadora']
    search_fields = ['nombre_curso', 'descripcion_curso', 'entidad_patrocinadora']


@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ['nombre_recurso', 'clasificador', 'activo']
    list_filter = ['clasificador', 'activo']
    search_fields = ['nombre_recurso', 'descripcion']


@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'fecha_producto', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre_producto', 'descripcion']


@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'estado_producto', 'valor_del_bien', 'activo']
    list_filter = ['estado_producto', 'activo']
    search_fields = ['nombre_producto', 'descripcion']


@admin.register(ReferenciaPersonal)
class ReferenciaPersonalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'email', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre', 'email']
