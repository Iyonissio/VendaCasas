from django.db import models
from django.utils.timezone import now
#from ..realtors.models import Corretor_de_Imoveis
#from backend.realest_estate.realtors.models import Corretor_de_Imoveis

class Lista(models.Model):
    class Tipo_De_Venda(models.TextChoices):
        PARA_VENDA = 'Para Venda'
        PARA_ALUGAR = 'Para alugar'

    class Tipo_De_Casa(models.TextChoices):
        CASASIMPLES = 'Casa Simples'
        CONDOMINIO = 'Condominio'
        PRAIA = 'Praia'
        APARTAMENTO = 'Apartamento'

    corretor_de_imoveis = models.ForeignKey('realtors.Corretor_de_Imoveis', on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    titulo = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)
    provincia = models.CharField(max_length=150)
    distrito = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=15)
    descricao = models.TextField(blank=True)
    tipo_de_venda = models.CharField(max_length=50, choices=Tipo_De_Venda.choices,default=Tipo_De_Venda.PARA_VENDA)
    preco = models.IntegerField()
    quartos = models.IntegerField()
    banheiros = models.DecimalField(max_digits=2,decimal_places=1)
    tipo_de_casa = models.CharField(max_length=50, choices=Tipo_De_Casa.choices, default=Tipo_De_Casa.CASASIMPLES)
    sqft = models.IntegerField()
    casa_aberta = models.BooleanField(default=False)
    foto_principal = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_7 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_8 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_9 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_10 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_11 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_12 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_13 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_14 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_15 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_16 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_17 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_18 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_19 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foto_20 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    foi_publicado = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.titulo

