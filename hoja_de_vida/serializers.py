from rest_framework import serializers
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


class DatosPersonalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPersonales
        fields = '__all__'


class FormacionAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormacionAcademica
        fields = '__all__'


class ExperienciaLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaLaboral
        fields = '__all__'


class ReferenciaPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenciaPersonal
        fields = '__all__'


class ReconocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reconocimiento
        fields = '__all__'


class CursoRealizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoRealizado
        fields = '__all__'


class ProductoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoAcademico
        fields = '__all__'


class ProductoLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoLaboral
        fields = '__all__'


class VentaGarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaGarage
        fields = '__all__'
