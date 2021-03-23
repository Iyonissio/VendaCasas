from django.contrib import admin
from .models import Lista

class ListaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','foi_publicado','preco','list_date','corretor_de_imoveis')
    list_display_links = ('id',)
    list_filter = ('corretor_de_imoveis','titulo')
    list_editable = ('foi_publicado','titulo')
    search_fields = ('titulo','descricao','endereco','provincia','zipcode','preco')
    list_per_page = 25

admin.site.register(Lista ,ListaAdmin)
