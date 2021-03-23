from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class SignupView(APIView):
    permissions_classes = (permissions.AllowAny)

    def post(self, request, format=None):
        data = self.request.data

        nome = data['nome']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email ja Existe Cadastrado'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password muito curto deve ter no minim 6 caracteres'})
                else:
                    user = User.objects.create_user(email=email, password=password,nome=nome)

                    user.save()
                    return Response({'success': 'Usuario Criado com sucesso'})
        else:
            return Response({'error':'Passwords Incoreta'})
