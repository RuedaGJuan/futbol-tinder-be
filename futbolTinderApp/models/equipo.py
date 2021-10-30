from django.db import models
from .user import User

class Equipo(models.Model):
    id_equipo = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(User, related_name='id_user', on_delete=models.CASCADE)
    nombre_equipo = models.CharField(max_length=20)
    cantidad_jugadores = models.IntegerField(default=0)
    rating_equipo = models.DecimalField(default=0.0, decimal_places=3, max_digits=10)
    localidades = [
        ('T', 'Tunjuelito'),
        ('K', 'Kennedy'),
        ('E', 'Engativa'),
        ('M', 'Martires')
    ]
    localidad = models.CharField(max_length=1, choices=localidades, default='T')