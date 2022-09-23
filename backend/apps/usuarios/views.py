from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import PerfilSerializer

from .models import Perfil

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()