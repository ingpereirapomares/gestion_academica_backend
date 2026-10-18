from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Programa
from .seriallizers import ProgramaSerializer

class Loginview(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'message': 'Inicio de sesión exitoso'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        

class ProgramaView(APIView):
    def get(self, request):
        programas_queryset=Programa.objects.all()
        serializer=ProgramaSerializer(programas_queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 