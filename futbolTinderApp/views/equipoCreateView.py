from django.conf                                      import settings
from django.http import request
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from futbolTinderApp.models.user                    import User
from futbolTinderApp.models.equipo                import Equipo
from futbolTinderApp.serializers.equipoSerializer import EquipoSerializer

class EquipoCreateView(generics.CreateAPIView):
    queryset           = Equipo.objects.all()
    serializer_class   = EquipoSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != int(request.data['user_id']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = EquipoSerializer(data=request.data['equipo_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Equipo creado", status=status.HTTP_201_CREATED)