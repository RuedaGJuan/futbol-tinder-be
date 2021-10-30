from django.contrib import admin
from .models.user import User
from .models.equipo import Equipo
from .models.jugador import Jugador
from .models.convocatoria import Convocatoria


# Register your models here.

admin.site.register(User) 
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Convocatoria)
