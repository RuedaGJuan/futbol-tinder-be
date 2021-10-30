from django.db import models
from .equipo import Equipo


class Convocatoria(models.Model):
    id_convocatoria = models.BigAutoField(primary_key=True)
    nombre_equipo = models.ForeignKey(Equipo, related_name='nombre_equipo_solicita', on_delete=models.CASCADE)
    fecha_convocatoria = models.DateTimeField()
    posiciones_requeridas = [
        ('AR', 'Arquero'),
        ('LA', 'Lateral'),
        ('CA', 'Carrilero'),
        ('DF', 'Defensa Central'),
        ('VR', 'Volante de Recuperacion'),
        ('VC', 'Volante de Creacion'),
        ('VO', 'Volante Ofensivo'),
        ('DE', 'Delantero')
    ]
    posicion_requerida = models.CharField(max_length=2, choices=posiciones_requeridas, default='DE')