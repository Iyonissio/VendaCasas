from django.contrib import admin
from .models import Corretor_de_Imoveis

class Corretor_de_ImoveisAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','data_de_contratacao')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 25

admin.site.register(Corretor_de_Imoveis, Corretor_de_ImoveisAdmin)
