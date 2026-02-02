from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class DatosPersonales(models.Model):
    SEXO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ]
    
    descripcion_perfil = models.CharField(max_length=50, blank=True, null=True)
    perfil_activo = models.BooleanField(default=True)
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20, blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=60, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_cedula = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    estado_civil = models.CharField(max_length=50, blank=True, null=True)
    licencia_conducir = models.CharField(max_length=6, blank=True, null=True)
    telefono_convencional = models.CharField(max_length=15, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=50, blank=True, null=True)
    direccion_domiciliaria = models.CharField(max_length=50, blank=True, null=True)
    sitio_web = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    titulo_profesional = models.CharField(max_length=200, blank=True, null=True)
    perfil = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='perfil/', blank=True, null=True)
    
    # Section Toggles
    mostrar_perfil = models.BooleanField(default=True)
    mostrar_experiencia = models.BooleanField(default=True)
    mostrar_formacion = models.BooleanField(default=True)
    mostrar_referencias = models.BooleanField(default=True)
    mostrar_reconocimientos = models.BooleanField(default=True)
    mostrar_cursos = models.BooleanField(default=True)
    mostrar_productos_academicos = models.BooleanField(default=True)
    mostrar_productos_laborales = models.BooleanField(default=True)
    mostrar_venta_garage = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if self.fecha_nacimiento and self.fecha_nacimiento > timezone.now().date():
            raise ValidationError({'fecha_nacimiento': "La fecha de nacimiento no puede estar en el futuro."})

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
    class Meta:
        verbose_name = "Datos Personales"
        verbose_name_plural = "Datos Personales"


class FormacionAcademica(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='formaciones', blank=True, null=True)
    nivel = models.CharField(max_length=100)
    institucion = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nivel} - {self.institucion}"
    
    class Meta:
        verbose_name = "Formación Académica"
        verbose_name_plural = "Formaciones Académicas"


class ExperienciaLaboral(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='experiencias', blank=True, null=True)
    cargo_desempenado = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=50)
    lugar_empresa = models.CharField(max_length=50, blank=True, null=True)
    email_empresa = models.CharField(max_length=100, blank=True, null=True)
    sitio_web_empresa = models.CharField(max_length=100, blank=True, null=True)
    nombre_contacto_empresarial = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto_empresarial = models.CharField(max_length=60, blank=True, null=True)
    fecha_inicio_gestion = models.DateField(blank=True, null=True)
    fecha_fin_gestion = models.DateField(blank=True, null=True)
    descripcion_funciones = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    ruta_certificado = models.FileField(upload_to='certificados/', blank=True, null=True)

    def clean(self):
        super().clean()
        hoy = timezone.now().date()
        if self.fecha_inicio_gestion and self.fecha_inicio_gestion > hoy:
            raise ValidationError({'fecha_inicio_gestion': "La fecha de inicio no puede estar en el futuro."})
        if self.fecha_fin_gestion and self.fecha_fin_gestion > hoy:
            raise ValidationError({'fecha_fin_gestion': "La fecha de fin no puede estar en el futuro."})
        if self.fecha_inicio_gestion and self.fecha_fin_gestion and self.fecha_inicio_gestion > self.fecha_fin_gestion:
            raise ValidationError({'fecha_fin_gestion': "La fecha de fin debe ser posterior a la fecha de inicio."})

    def __str__(self):
        return f"{self.cargo_desempenado} en {self.nombre_empresa}"
    
    class Meta:
        verbose_name = "Experiencia Laboral"
        verbose_name_plural = "Experiencias Laborales"
        ordering = ['-fecha_inicio_gestion', 'nombre_empresa']


class Reconocimiento(models.Model):
    TIPO_CHOICES = [
        ('Académico', 'Académico'),
        ('Público', 'Público'),
        ('Privado', 'Privado'),
    ]
    
    datos_personales = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='reconocimientos', blank=True, null=True)
    tipo_reconocimiento = models.CharField(max_length=100, choices=TIPO_CHOICES)
    fecha_reconocimiento = models.DateField(blank=True, null=True)
    descripcion_reconocimiento = models.CharField(max_length=100, blank=True, null=True)
    entidad_patrocinadora = models.CharField(max_length=100, blank=True, null=True)
    nombre_contacto_auspicia = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto_auspicia = models.CharField(max_length=60, blank=True, null=True)
    activo = models.BooleanField(default=True)
    ruta_certificado = models.FileField(upload_to='reconocimientos/', blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_reconocimiento} - {self.descripcion_reconocimiento}"
    
    class Meta:
        verbose_name = "Reconocimiento"
        verbose_name_plural = "Reconocimientos"


class CursoRealizado(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='cursos', blank=True, null=True)
    nombre_curso = models.CharField(max_length=100)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    total_horas = models.IntegerField(blank=True, null=True)
    descripcion_curso = models.CharField(max_length=100, blank=True, null=True)
    entidad_patrocinadora = models.CharField(max_length=100, blank=True, null=True)
    nombre_contacto_auspicia = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto_auspicia = models.CharField(max_length=60, blank=True, null=True)
    email_empresa_patrocinadora = models.CharField(max_length=60, blank=True, null=True)
    activo = models.BooleanField(default=True)
    ruta_certificado = models.FileField(upload_to='cursos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_curso} - {self.entidad_patrocinadora}"
    
    class Meta:
        verbose_name = "Curso Realizado"
        verbose_name_plural = "Cursos Realizados"


class ProductoAcademico(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='productos_academicos', blank=True, null=True)
    nombre_recurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_recurso}"
    
    class Meta:
        verbose_name = "Producto Académico"
        verbose_name_plural = "Productos Académicos"


class ProductoLaboral(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='productos_laborales', blank=True, null=True)
    nombre_producto = models.CharField(max_length=100)
    fecha_producto = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_producto}"
    
    class Meta:
        verbose_name = "Producto Laboral"
        verbose_name_plural = "Productos Laborales"


class VentaGarage(models.Model):
    ESTADO_CHOICES = [
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
    ]
    
    datos_personales = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='ventas_garage', blank=True, null=True)
    nombre_producto = models.CharField(max_length=100)
    estado_producto = models.CharField(max_length=40, choices=ESTADO_CHOICES)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    valor_del_bien = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='venta_garage/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_producto} - ${self.valor_del_bien}"
    
    class Meta:
        verbose_name = "Venta Garage"
        verbose_name_plural = "Ventas Garage"


class ReferenciaPersonal(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, related_name='referencias', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Referencia Personal"
        verbose_name_plural = "Referencias Personales"
