from rest_framework import serializers
from .models import Lista

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ('titulo','endereco','provincia','distrito','preco','tipo_de_venda','tipo_de_casa','quartos','banheiros','sqft','foto_principal','slug')

class ListaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'
        lookup_field = 'slug'