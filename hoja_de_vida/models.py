from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class DatosPersonales(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    titulo_profesional = models.CharField(max_length=200, blank=True, null=True)
    perfil = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='perfil/', blank=True, null=True)
    
    # Section Toggles
    mostrar_perfil = models.BooleanField(default=True)
    mostrar_experiencia = models.BooleanField(default=True)
    mostrar_formacion = models.BooleanField(default=True)
    mostrar_referencias = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if self.fecha_nacimiento and self.fecha_nacimiento > timezone.now().date():
            raise ValidationError({'fecha_nacimiento': "La fecha de nacimiento no puede estar en el futuro."})

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class FormacionAcademica(models.Model):
    nivel = models.CharField(max_length=100)
    institucion = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"

class ExperienciaLaboral(models.Model):
    empresa = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    certificado = models.FileField(upload_to='certificados/', blank=True, null=True)

    def clean(self):
        super().clean()
        hoy = timezone.now().date()
        if self.fecha_inicio and self.fecha_inicio > hoy:
            raise ValidationError({'fecha_inicio': "La fecha de inicio no puede estar en el futuro."})
        if self.fecha_fin and self.fecha_fin > hoy:
            raise ValidationError({'fecha_fin': "La fecha de fin no puede estar en el futuro."})
        if self.fecha_inicio and self.fecha_fin and self.fecha_inicio > self.fecha_fin:
            raise ValidationError({'fecha_fin': "La fecha de fin debe ser posterior a la fecha de inicio."})

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"

class ReferenciaPersonal(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre
