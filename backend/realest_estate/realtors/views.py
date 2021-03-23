from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions
from .models import Corretor_de_Imoveis
from .serializers import Corretor_de_ImoveisSerializer

class Corretor_de_ImoveisListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Corretor_de_Imoveis.objects.all()
    serializer_class = Corretor_de_ImoveisSerializer
    pagination_class = None

class Corretor_de_ImoveisView(RetrieveAPIView):
    queryset = Corretor_de_Imoveis.objects.all()
    serializer_class = Corretor_de_ImoveisSerializer

class MaisVendidosView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Corretor_de_Imoveis.objects.filter(mais_vendido=True)
    serializer_class = Corretor_de_ImoveisSerializer
    pagination_class = None
