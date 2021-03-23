from rest_framework import serializers
from .models import Corretor_de_Imoveis

class Corretor_de_ImoveisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corretor_de_Imoveis
        fields = '__all__'