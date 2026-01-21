import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.settings')
django.setup()

from hoja_de_vida.models import DatosPersonales, FormacionAcademica, ExperienciaLaboral, ReferenciaPersonal

def poblar_datos():
    # Datos Personales
    print("Poblando Datos Personales...")
    DatosPersonales.objects.all().delete()
    DatosPersonales.objects.create(
        nombres="YANDRI YAIR",
        apellidos="MACIAS VELEZ",
        estado_civil="SOLTERO",
        cedula="135193423-5",
        fecha_nacimiento="1999-02-21",
        edad=26,
        direccion="Manta - Nuevo Tarqui - 5 de junio",
        telefono="0999380605",
        email="yairvelez050@gmail.com"
    )

    # Formacion Academica
    print("Poblando Formación Académica...")
    FormacionAcademica.objects.all().delete()
    FormacionAcademica.objects.create(
        nivel="BACHILLERATO TECNICO EN APLICACIONES INFORMATICAS",
        institucion="UNIDAD EDUCATIVA LIBERTAD DE TIMBRE",
        titulo="",
        estado="CULMINADO"
    )
    FormacionAcademica.objects.create(
        nivel="ING. TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION",
        institucion="UNIVERSIDAD LAICA ELOY ALFARO DE MANABI",
        titulo="",
        estado="ACTUALMENTE CURSANDO"
    )

    # Experiencia Laboral
    print("Poblando Experiencia Laboral...")
    ExperienciaLaboral.objects.all().delete()
    ExperienciaLaboral.objects.create(
        empresa="LOTERA NACIONAL cc.multiplaza",
        cargo="ATENCION AL CLIENTE",
        descripcion="ATENCION AL CLIENTE EN LOCAL DE LOTERA NACIONAL cc.multiplaza"
    )

    # Referencias Personales
    print("Poblando Referencias Personales...")
    ReferenciaPersonal.objects.all().delete()
    ReferenciaPersonal.objects.create(
        nombre="GESSLAINE CEDEÑO",
        telefono="0968343602",
        email="gesslayne@gmail.com"
    )
    ReferenciaPersonal.objects.create(
        nombre="DENISSE MACIAS",
        telefono="0998478481"
    )

    print("Población de datos completada.")

if __name__ == '__main__':
    poblar_datos()
