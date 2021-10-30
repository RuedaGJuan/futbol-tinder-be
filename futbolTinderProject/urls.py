from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from futbolTinderApp import views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('equipo/create/', views.EquipoCreateView.as_view()),
    path('jugador/create/', views.JugadorCreateView.as_view()),
    path('convocatoria/create/', views.ConvocatoriaCreateView.as_view()),
    path('convocatoria/<int:user>/<int:pk>/', views.ConvocatoriaDetailView.as_view()),
    path('listaConvocatorias/', views.ConvocatoriaListView.as_view()),
    path('convocatoria/update/<int:user>/<int:pk>/', views.ConvocatoriaUpdateView.as_view()),
    path('convocatoria/remove/<int:user>/<int:pk>/', views.ConvocatoriaDeleteView.as_view())
]