from django.db import models
from datetime import datetime

class Corretor_de_Imoveis(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='photos/%Y/%m/%d')
    descricao = models.TextField(blank=True)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    mais_vendido = models.BooleanField(default=False)
    data_de_contratacao = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome
