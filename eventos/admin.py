from django.contrib import admin
from .models import Evento

admin.site.site_header = "Administração do Suporte"

class ListandoEvento(admin.ModelAdmin):
    list_display = ("nome", "tempo", "descricao")
    list_display_links = ("tempo","nome")
    search_fields = ("nome",)
    list_filter = ("status","tempo")
    list_per_page = 20

admin.site.register(Evento, ListandoEvento)