# Generated by Django 3.1.1 on 2021-03-22 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corretor_de_Imoveis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('descricao', models.TextField(blank=True)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('mais_vendido', models.BooleanField(default=False)),
                ('data_de_contratacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
