from django.contrib import admin
from django.contrib import messages

from base.models import Contato

@admin.action(description='Marcar Formulário(s) de Contato com lido(s)')
def marcar_como_lido(Modeladmin, request, queryset):
    queryset.update(lido=True)
    Modeladmin.message_user(request, 'Marcar Formulário(s) de Contato com lido(s)', messages.SUCCESS)


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'lido', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data', 'lido']
    actions = [marcar_como_lido]