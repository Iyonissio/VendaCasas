from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import message, send_mail
from rest_framework.response import Response

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            send_mail(
                data['subjet'],
                'Nome: '
                + data['nome']
                + '\nEmail: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                'mbryoyo01@gmail.com',
                ['mbryoyo01@gmail.com'],
                fail_silently=False
            )
            contact = Contact(nome=data['nome'], email=data['email'], subjet=data['subject'], message=data['message'])
            contact.save()

            return Response({'sucesso': 'Mensagem enviada com sucesso'})
        
        except:
            return Response ({'error': 'Falhou no envio da mensagem'})












