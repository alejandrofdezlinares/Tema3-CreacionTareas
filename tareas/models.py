from django.db import models



class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128, default='')
    fecha_registro = models.DateTimeField()

   
    proyectos_asignados = models.ManyToManyField(
        'Proyecto',
        related_name='colaboradores',
        blank=True
    )

    def __str__(self):
        return self.nombre



class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()

    creador = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='proyectos_creados'
    )

    def __str__(self):
        return self.nombre



class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre



class Tarea(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Pendiente'
    )

    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()

    creador = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='tareas_creadas'
    )

  
    usuarios_asignados = models.ManyToManyField(
        Usuario,
        through='AsignacionTarea',
        related_name='tareas_asignadas'
    )

 
    etiquetas = models.ManyToManyField(
        Etiqueta,
        related_name='tareas',
        blank=True
    )

   
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='tareas'
    )

    def __str__(self):
        return self.titulo



class AsignacionTarea(models.Model):

  
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField()

    def __str__(self):
        return f'{self.usuario} - {self.tarea}'



class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField()

  
    autor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

   
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

    def __str__(self):
        return self.contenido[:50]