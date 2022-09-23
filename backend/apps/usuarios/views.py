from django.contrib.auth import authenticate, login
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AgenteSerializer
from .models import Agente


class AgenteViewSet(viewsets.ModelViewSet):
    serializer_class = AgenteSerializer
    queryset = Agente.objects.all()


class LoginView(APIView):
    def post(self, request):
        # * Obtener los datos del request
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        
        # * Validar que los datos sean correctos
        user = authenticate(username=username, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            print(request.user)
            return Response(status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(status=status.HTTP_404_NOT_FOUND)
