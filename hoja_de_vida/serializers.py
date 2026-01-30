from rest_framework import serializers
from .models import DatosPersonales, FormacionAcademica, ExperienciaLaboral, ReferenciaPersonal

class DatosPersonalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPersonales
        fields = ['nombres', 'apellidos', 'estado_civil', 'cedula', 'fecha_nacimiento', 'edad', 'direccion', 'telefono', 'email', 'titulo_profesional', 'perfil']

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
