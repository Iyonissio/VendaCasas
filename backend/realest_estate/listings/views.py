from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions
from .models import Lista
from .serializers import ListaSerializer, ListaDetailSerializer
from datetime import datetime, timezone,timedelta

class ListasView(ListAPIView):
    queryset = Lista.objects.order_by('-list_date').filter(foi_publicado=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListaSerializer
    lookup_field = 'slug'

class ListaView(RetrieveAPIView):
    queryset = Lista.objects.order_by('-list_date').filter(foi_publicado=True)
    serializer_class = ListaDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListaSerializer

    def post(self, request, format=None):
        queryset = Lista.objects.order_by('-list_date').filter(foi_publicado=True)
        data = self.request.data

        tipo_de_venda = data['tipo_de_venda']
        queryset = queryset.filter(tipo_de_venda__iexact=tipo_de_venda)

        preco = data['preco']
        if preco == '$0+':
            preco = 0
        elif preco == '$200,000+':
            preco = 200000
        elif preco == '$400,000+':
            preco = 400000
        elif preco == '$600,000+':
            preco = 600000
        elif preco == '$800,000+':
            preco = 800000
        elif preco == '$1000,000+':
            preco = 1000000
        elif preco == '$1,500,000+':
            preco = 1500000
        elif preco == 'Any':
            preco = -1

        if preco != -1:
            queryset = queryset.filter(preco__gte=preco)

        quartos = data['quartos']
        if quartos == '0+':
            quartos = 0
        elif quartos == '1+':
            quartos = 1
        elif quartos == '2+':
            quartos = 2
        elif quartos == '3+':
            quartos = 3
        elif quartos == '4+':
            quartos = 4
        elif quartos == '5+':
            quartos = 5

        queryset = queryset.filter(quartos__gte=quartos)

        tipo_de_casa = data['tipo_de_casa']
        queryset =queryset.filter(tipo_de_casa__iexact=tipo_de_casa)

        banheiros = data['banheiros']
        if banheiros == '0+':
            banheiros = 0.0
        elif banheiros == '1+':
            banheiros = 1.0
        elif banheiros == '2+':
            banheiros = 2.0
        elif banheiros == '3+':
            banheiros = 3.0
        elif banheiros == '4+':
            banheiros = 4.0

        queryset = queryset.filter(banheiros__gte=banheiros)

        sqft = data['sqft']
        if sqft == '1000+':
            sqft = 1000
        elif sqft == '1200+':
            sqft = 1200
        elif sqft == '1500+':
            sqft = 1500
        elif sqft == '2000+':
            sqft = 2000
        elif sqft == 'Any+':
            sqft = 0

        if sqft != 0:
            queryset = queryset.filter(sqft__gte=banheiros)

        days_passed = data['days_listed']
        if days_passed == '1 or less':
            days_passed = 1
        elif days_passed == '2 or less':
            days_passed = 2
        elif days_passed == '5 or less':
            days_passed = 5
        elif days_passed == '10 or less':
            days_passed = 10
        elif days_passed == '20 or less':
            days_passed = 20
        elif days_passed == 'Any':
            days_passed = 0

        for query in queryset:
            num_days = (datetime.now(timezone.utc) - query.list_date).days

            if days_passed != 0:
                if num_days > days_passed:
                    slug=query.slug
                    queryset = queryset.exclude(slug__iexact=slug)

        has_photos = data['has_photos']
        if has_photos =='1+':
            has_photos = 1
        elif has_photos == '3+':
            has_photos = 3
        elif has_photos == '5+':
            has_photos = 5
        elif has_photos == '10+':
            has_photos = 10
        elif has_photos == '15+':
            has_photos = 15

        for query in queryset:
            count = 0
            if query.foto_1:
                count += 1
            if query.foto_2:
                count += 1
            if query.foto_3:
                count += 1
            if query.foto_4:
                count += 1
            if query.foto_5:
                count += 1
            if query.foto_6:
                count += 1
            if query.foto_7:
                count += 1
            if query.foto_8:
                count += 1
            if query.foto_9:
                count += 1
            if query.foto_10:
                count += 1
            if query.foto_11:
                count += 1
            if query.foto_12:
                count += 1
            if query.foto_13:
                count += 1
            if query.foto_14:
                count += 1
            if query.foto_15:
                count += 1
            if query.foto_16:
                count += 1
            if query.foto_17:
                count += 1
            if query.foto_18:
                count += 1
            if query.foto_19:
                count += 1
            if query.foto_20:
                count += 1

            if count < has_photos:
                slug = query.slug
                queryset = queryset.exclude(slug__iexact=slug)

        casa_aberta = data['casa_aberta']
        queryset = queryset.filter(casa_aberta__iexact=casa_aberta)

        keywords = data['keywords']
        queryset =queryset.filter(descricao__icontains=keywords)

        serializer = ListaSerializer(queryset, many=True)

        return Response(serializer.data)
