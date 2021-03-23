# Generated by Django 3.1.1 on 2021-03-23 17:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('titulo', models.CharField(max_length=150)),
                ('endereco', models.CharField(max_length=150)),
                ('provincia', models.CharField(max_length=150)),
                ('distrito', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=15)),
                ('descricao', models.TextField(blank=True)),
                ('tipo_de_venda', models.CharField(choices=[('Para Venda', 'Para Venda'), ('Para alugar', 'Para Alugar')], default='Para Venda', max_length=50)),
                ('preco', models.IntegerField()),
                ('quartos', models.IntegerField()),
                ('banheiros', models.DecimalField(decimal_places=1, max_digits=2)),
                ('tipo_de_casa', models.CharField(choices=[('Casa Simples', 'Casasimples'), ('Condominio', 'Condominio'), ('Praia', 'Praia'), ('Apartamento', 'Apartamento')], default='Casa Simples', max_length=50)),
                ('sqft', models.IntegerField()),
                ('casa_aberta', models.BooleanField(default=False)),
                ('foto_principal', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_9', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_10', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_11', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_12', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_13', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_14', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_15', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_16', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_17', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_18', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_19', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foto_20', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('foi_publicado', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('corretor_de_imoveis', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.corretor_de_imoveis')),
            ],
        ),
    ]