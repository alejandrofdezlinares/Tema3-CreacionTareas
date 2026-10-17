import os
import django
import random
from datetime import date, time, datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_tareas.settings')
django.setup()

from tareas.models import Usuario, Proyecto, Etiqueta, Tarea, AsignacionTarea, Comentario

usuarios = []

for i in range(1, 31):
    usuario, creado = Usuario.objects.get_or_create(
        correo_electronico=f'usuario{i}@ejemplo.com',
        defaults={
            'nombre': f'Usuario {i}',
            'contrasena': f'Clave{i}123',
            'fecha_registro': datetime.now()
        }
    )
    usuarios.append(usuario)

proyectos = []

for i in range(1, 31):
    proyecto, creado = Proyecto.objects.get_or_create(
        nombre=f'Proyecto {i}',
        defaults={
            'descripcion': f'Descripcion del proyecto {i}',
            'duracion_estimada': float(random.randint(1, 100)),
            'fecha_inicio': date.today(),
            'fecha_finalizacion': date.today() + timedelta(days=30),
            'creador': usuarios[i - 1]
        }
    )
    proyecto.colaboradores.add(usuarios[(i) % 30])
    proyectos.append(proyecto)

etiquetas = []

for i in range(1, 31):
    etiqueta, creado = Etiqueta.objects.get_or_create(
        nombre=f'Etiqueta {i}'
    )
    etiquetas.append(etiqueta)

tareas = []

for i in range(1, 31):
    tarea, creado = Tarea.objects.get_or_create(
        titulo=f'Tarea {i}',
        defaults={
            'descripcion': f'Descripcion de la tarea {i}',
            'prioridad': random.randint(1, 5),
            'estado': random.choice(['Pendiente', 'Progreso', 'Completada']),
            'completada': i % 3 == 0,
            'fecha_creacion': date.today(),
            'hora_vencimiento': time(12, 0),
            'creador': usuarios[i - 1],
            'proyecto': proyectos[i - 1]
        }
    )
    tarea.usuarios_asignados.add(
        usuarios[(i) % 30],
        through_defaults={
            'observaciones': f'Asignacion de la tarea {i}',
            'fecha_asignacion': datetime.now()
        }
    )
    tarea.etiquetas.add(etiquetas[i - 1])
    tareas.append(tarea)

for i in range(1, 31):
    AsignacionTarea.objects.get_or_create(
        tarea=tareas[i - 1],
        usuario=usuarios[(i) % 30],
        defaults={
            'observaciones': f'Asignacion de la tarea {i}',
            'fecha_asignacion': datetime.now()
        }
    )

for i in range(1, 31):
    Comentario.objects.get_or_create(
        contenido=f'Comentario de ejemplo {i}',
        defaults={
            'fecha_comentario': datetime.now()
        }
    )

print('Datos de ejemplo generados correctamente.')

