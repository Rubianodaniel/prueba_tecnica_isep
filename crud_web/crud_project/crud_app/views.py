from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Validate
from .serializers import ValidateSerializer

class ValidateListCreateView(generics.ListCreateAPIView):
    """
    Vista que permite listar y crear objetos de la clase Validate.

    Métodos permitidos:
    - GET: Obtiene una lista de objetos Validate existentes.
    - POST: Crea un nuevo objeto Validate.

    Atributos:
    - queryset: Consulta de base de datos que selecciona todos los objetos Validate.
    - serializer_class: Clase de serializador utilizada para la representación JSON de los objetos Validate.
    """
        
    queryset = Validate.objects.all()
    serializer_class = ValidateSerializer

class ValidateUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):

    """
    Vista que permite recuperar, actualizar y eliminar objetos Validate.

    Métodos permitidos:
    - GET: Obtiene un objeto Validate específico.
    - PUT: Actualiza un objeto Validate existente.
    - PATCH: Actualiza parcialmente un objeto Validate existente.
    - DELETE: Elimina un objeto Validate existente.

    Atributos:
    - queryset: Consulta de base de datos que selecciona todos los objetos Validate.
    - serializer_class: Clase de serializador utilizada para la representación JSON de los objetos Validate.
    """
    queryset = Validate.objects.all()
    serializer_class = ValidateSerializer
