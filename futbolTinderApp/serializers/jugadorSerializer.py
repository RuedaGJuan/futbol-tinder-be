from rest_framework import serializers 
from futbolTinderApp.models import Jugador


class JugadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jugador
        fields = [
                'alias',
                'fecha_nacimiento',
                'estatura',
                'peso',
                'posicion',
                'id_user']