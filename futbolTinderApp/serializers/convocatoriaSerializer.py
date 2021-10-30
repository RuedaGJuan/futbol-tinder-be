from rest_framework import serializers 
from futbolTinderApp.models import Convocatoria


class ConvocatoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Convocatoria
        fields = [
                'fecha_convocatoria', #Formato: "2021-10-24 18:00"
                'posicion_requerida',
                'nombre_equipo' 
                ]