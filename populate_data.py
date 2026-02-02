import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuracion.settings')
django.setup()

from hoja_de_vida.models import (
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


def poblar_datos():
    # Datos Personales
    print("Poblando Datos Personales...")
    DatosPersonales.objects.all().delete()
    datos = DatosPersonales.objects.create(
        descripcion_perfil="Perfil Profesional TIC",
        perfil_activo=True,
        nombres="YANDRI YAIR",
        apellidos="MACIAS VELEZ",
        nacionalidad="Ecuatoriana",
        lugar_nacimiento="Manta, Ecuador",
        fecha_nacimiento="1999-02-21",
        numero_cedula="1351934235",
        sexo="H",
        estado_civil="SOLTERO",
        licencia_conducir="Tipo B",
        telefono_convencional="0999380605",
        telefono_fijo="",
        direccion_trabajo="",
        direccion_domiciliaria="Manta - Nuevo Tarqui - 5 de junio",
        sitio_web="",
        email="yairvelez050@gmail.com",
        titulo_profesional="INGENIERO EN TECNOLOGÍAS DE LA INFORMACIÓN Y LA COMUNICACIÓN",
        perfil="Estudiante apasionado por las tecnologías de la información con experiencia en atención al cliente y logística. Enfocado en el desarrollo continuo y la aplicación de soluciones tecnológicas eficaces.",
        mostrar_perfil=True,
        mostrar_experiencia=True,
        mostrar_formacion=True,
        mostrar_referencias=True,
        mostrar_reconocimientos=True,
        mostrar_cursos=True,
        mostrar_productos_academicos=True,
        mostrar_productos_laborales=True,
        mostrar_venta_garage=True,
    )

    # Formacion Academica
    print("Poblando Formación Académica...")
    FormacionAcademica.objects.all().delete()
    FormacionAcademica.objects.create(
        datos_personales=datos,
        nivel="BACHILLERATO TECNICO EN APLICACIONES INFORMATICAS",
        institucion="UNIDAD EDUCATIVA LIBERTAD DE TIMBRE",
        titulo="Bachiller Técnico",
        estado="CULMINADO",
        activo=True
    )
    FormacionAcademica.objects.create(
        datos_personales=datos,
        nivel="ING. TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION",
        institucion="UNIVERSIDAD LAICA ELOY ALFARO DE MANABI",
        titulo="Ingeniero en TIC",
        estado="ACTUALMENTE CURSANDO",
        activo=True
    )

    # Experiencia Laboral
    print("Poblando Experiencia Laboral...")
    ExperienciaLaboral.objects.all().delete()
    ExperienciaLaboral.objects.create(
        datos_personales=datos,
        cargo_desempenado="ATENCION AL CLIENTE",
        nombre_empresa="LOTERIA NACIONAL",
        lugar_empresa="CC. MULTIPLAZA, Manta",
        email_empresa="",
        sitio_web_empresa="",
        nombre_contacto_empresarial="",
        telefono_contacto_empresarial="",
        fecha_inicio_gestion="2022-01-15",
        fecha_fin_gestion="2022-06-30",
        descripcion_funciones="Atención al cliente en local de Lotería Nacional ubicado en el centro comercial Multiplaza.",
        activo=True
    )
    ExperienciaLaboral.objects.create(
        datos_personales=datos,
        cargo_desempenado="ATENCION AL CLIENTE",
        nombre_empresa="CC",
        lugar_empresa="Manta",
        descripcion_funciones="Atención al cliente y soporte general.",
        activo=True
    )
    ExperienciaLaboral.objects.create(
        datos_personales=datos,
        cargo_desempenado="AUXILIAR DE BODEGA",
        nombre_empresa="DISTRIBUIDORA DE ALIMENTOS Y BEBIDAS S.A. (DABSA)",
        lugar_empresa="Manta",
        fecha_inicio_gestion="2023-03-01",
        fecha_fin_gestion="2023-12-31",
        descripcion_funciones="Trabajo en bodega, control de inventario, recepción y despacho de productos.",
        activo=True
    )

    # Referencias Personales
    print("Poblando Referencias Personales...")
    ReferenciaPersonal.objects.all().delete()
    ReferenciaPersonal.objects.create(
        datos_personales=datos,
        nombre="GESSLAINE CEDEÑO",
        telefono="0968343602",
        email="gesslayne@gmail.com",
        activo=True
    )
    ReferenciaPersonal.objects.create(
        datos_personales=datos,
        nombre="DENISSE MACIAS",
        telefono="0998478481",
        email="",
        activo=True
    )

    # Reconocimientos
    print("Poblando Reconocimientos...")
    Reconocimiento.objects.all().delete()
    Reconocimiento.objects.create(
        datos_personales=datos,
        tipo_reconocimiento="Académico",
        fecha_reconocimiento="2023-07-15",
        descripcion_reconocimiento="Mejor promedio del semestre",
        entidad_patrocinadora="Universidad Laica Eloy Alfaro de Manabí",
        activo=True
    )

    # Cursos Realizados
    print("Poblando Cursos Realizados...")
    CursoRealizado.objects.all().delete()
    CursoRealizado.objects.create(
        datos_personales=datos,
        nombre_curso="Desarrollo Web con Python y Django",
        fecha_inicio="2024-01-10",
        fecha_fin="2024-03-15",
        total_horas=80,
        descripcion_curso="Curso de desarrollo de aplicaciones web usando Django Framework",
        entidad_patrocinadora="Platzi",
        activo=True
    )
    CursoRealizado.objects.create(
        datos_personales=datos,
        nombre_curso="React JS Fundamentals",
        fecha_inicio="2024-04-01",
        fecha_fin="2024-05-30",
        total_horas=60,
        descripcion_curso="Fundamentos de React para desarrollo frontend",
        entidad_patrocinadora="Udemy",
        activo=True
    )

    # Productos Académicos
    print("Poblando Productos Académicos...")
    ProductoAcademico.objects.all().delete()
    ProductoAcademico.objects.create(
        datos_personales=datos,
        nombre_recurso="Sistema de Gestión de Inventarios",
        clasificador="Proyecto de Software",
        descripcion="Aplicación web para gestión de inventarios en pequeñas empresas",
        activo=True
    )

    # Productos Laborales
    print("Poblando Productos Laborales...")
    ProductoLaboral.objects.all().delete()
    ProductoLaboral.objects.create(
        datos_personales=datos,
        nombre_producto="Manual de Procesos de Bodega",
        fecha_producto="2023-11-01",
        descripcion="Documentación de procesos de recepción y despacho de productos",
        activo=True
    )

    # Venta Garage (ejemplo)
    print("Poblando Venta Garage...")
    VentaGarage.objects.all().delete()
    VentaGarage.objects.create(
        datos_personales=datos,
        nombre_producto="Laptop HP Pavilion",
        estado_producto="Bueno",
        descripcion="Laptop en buen estado, 8GB RAM, 256GB SSD",
        valor_del_bien=350.00,
        activo=True
    )

    print("Población de datos completada.")

    # Crear Superusuario
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        print("Creando superusuario 'admin'...")
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superusuario creado.")
    else:
        print("El superusuario 'admin' ya existe.")


if __name__ == '__main__':
    poblar_datos()
