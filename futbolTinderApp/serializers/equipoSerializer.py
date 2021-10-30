from rest_framework import serializers 
from futbolTinderApp.models import Equipo


class EquipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipo
        fields = [
                'nombre_equipo',
                'cantidad_jugadores',
                'localidad',
                'id_user'
                ]