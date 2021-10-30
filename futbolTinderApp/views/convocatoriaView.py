from django.conf                                      import settings
from django.http import request
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from futbolTinderApp.models.user                    import User
from futbolTinderApp.models.convocatoria                import Convocatoria
from futbolTinderApp.serializers.convocatoriaSerializer import ConvocatoriaSerializer

class ConvocatoriaDetailView(generics.RetrieveAPIView):
    queryset           = Convocatoria.objects.all()
    serializer_class   = ConvocatoriaSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

class ConvocatoriaListView(generics.ListAPIView):
    queryset           = Convocatoria.objects.all()
    serializer_class   = ConvocatoriaSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
                
        queryset = Convocatoria.objects.all()
        return queryset

class ConvocatoriaCreateView(generics.CreateAPIView):
    queryset           = Convocatoria.objects.all()
    serializer_class   = ConvocatoriaSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != int(request.data['user_id']):
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ConvocatoriaSerializer(data=request.data['convocatoria_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Convocatoria creada", status=status.HTTP_201_CREATED)

class ConvocatoriaUpdateView(generics.UpdateAPIView):
    queryset           = Convocatoria.objects.all()
    serializer_class   = ConvocatoriaSerializer
    permission_classes = (IsAuthenticated,)
    
    def put(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)

class ConvocatoriaDeleteView(generics.DestroyAPIView):
    queryset           = Convocatoria.objects.all()
    serializer_class   = ConvocatoriaSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)