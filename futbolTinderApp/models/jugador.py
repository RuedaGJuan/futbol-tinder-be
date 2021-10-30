from django.db import models
from .user import User

class Jugador(models.Model):
    id_jugador = models.BigAutoField(primary_key= True)
    alias = models.CharField('Alias', max_length=20 , unique=True)
    id_user = models.ForeignKey(User, related_name= 'id_jugador', on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    estatura = models.IntegerField(default=0)
    peso = models.IntegerField(default=0)
    posiciones = [
        ('AR', 'Arquero'),
        ('LA', 'Lateral'),
        ('CA', 'Carrilero'),
        ('DF', 'Defensa Central'),
        ('VR', 'Volante de Recuperacion'),
        ('VC', 'Volante de Creacion'),
        ('VO', 'Volante Ofensivo'),
        ('DE', 'Delantero')
    ]
    posicion = models.CharField(max_length=2, choices=posiciones, default='DE')
    rating_jugador = models.DecimalField(default=0.0, decimal_places=3, max_digits=10)