from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    DatosPersonales, 
    FormacionAcademica, 
    ExperienciaLaboral, 
    ReferenciaPersonal,
    Reconocimiento,
    CursoRealizado,
    ProductoAcademico,
    ProductoLaboral,
    VentaGarage,
)
from .serializers import (
    DatosPersonalesSerializer, 
    FormacionAcademicaSerializer, 
    ExperienciaLaboralSerializer, 
    ReferenciaPersonalSerializer,
    ReconocimientoSerializer,
    CursoRealizadoSerializer,
    ProductoAcademicoSerializer,
    ProductoLaboralSerializer,
    VentaGarageSerializer,
)


class IndexView(TemplateView):
    template_name = 'index.html'


@api_view(['GET'])
def cv_api(request):
    datos_personales = DatosPersonales.objects.filter(perfil_activo=True).first()
    
    # Solo mostrar elementos activos
    formacion = FormacionAcademica.objects.filter(activo=True)
    experiencia = ExperienciaLaboral.objects.filter(activo=True).order_by('-fecha_inicio_gestion', 'nombre_empresa')
    referencias = ReferenciaPersonal.objects.filter(activo=True)
    reconocimientos = Reconocimiento.objects.filter(activo=True)
    cursos = CursoRealizado.objects.filter(activo=True)
    productos_academicos = ProductoAcademico.objects.filter(activo=True)
    productos_laborales = ProductoLaboral.objects.filter(activo=True)
    ventas_garage = VentaGarage.objects.filter(activo=True)
    
    response_data = {
        'datos_personales': DatosPersonalesSerializer(datos_personales).data if datos_personales else None,
    }
    
    # Solo incluir secciones si están habilitadas en datos_personales
    if datos_personales:
        if datos_personales.mostrar_formacion:
            response_data['formacion'] = FormacionAcademicaSerializer(formacion, many=True).data
        if datos_personales.mostrar_experiencia:
            response_data['experiencia'] = ExperienciaLaboralSerializer(experiencia, many=True).data
        if datos_personales.mostrar_referencias:
            response_data['referencias'] = ReferenciaPersonalSerializer(referencias, many=True).data
        if datos_personales.mostrar_reconocimientos:
            response_data['reconocimientos'] = ReconocimientoSerializer(reconocimientos, many=True).data
        if datos_personales.mostrar_cursos:
            response_data['cursos'] = CursoRealizadoSerializer(cursos, many=True).data
        if datos_personales.mostrar_productos_academicos:
            response_data['productos_academicos'] = ProductoAcademicoSerializer(productos_academicos, many=True).data
        if datos_personales.mostrar_productos_laborales:
            response_data['productos_laborales'] = ProductoLaboralSerializer(productos_laborales, many=True).data
        if datos_personales.mostrar_venta_garage:
            response_data['ventas_garage'] = VentaGarageSerializer(ventas_garage, many=True).data
    else:
        # Si no hay datos personales, incluir todos los datos
        response_data['formacion'] = FormacionAcademicaSerializer(formacion, many=True).data
        response_data['experiencia'] = ExperienciaLaboralSerializer(experiencia, many=True).data
        response_data['referencias'] = ReferenciaPersonalSerializer(referencias, many=True).data
        response_data['reconocimientos'] = ReconocimientoSerializer(reconocimientos, many=True).data
        response_data['cursos'] = CursoRealizadoSerializer(cursos, many=True).data
        response_data['productos_academicos'] = ProductoAcademicoSerializer(productos_academicos, many=True).data
        response_data['productos_laborales'] = ProductoLaboralSerializer(productos_laborales, many=True).data
        response_data['ventas_garage'] = VentaGarageSerializer(ventas_garage, many=True).data
    
    return Response(response_data)
