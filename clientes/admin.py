from django.contrib import admin
from .models import Cliente


#@admin.register(Endereco)
#class EnderecoAdmin(admin.ModelAdmin):
#    list_display = ('endereco', 'numero', 'bairro',
#                    'cidade', 'estado'
#                    'criacao', 'atualizacao', 'delecao',
#                    'ativo',
#                    )


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dtaNascimento', 'CPF',
                    'RG', 'CEL', 'SEXO', 'email',
                    'criacao', 'atualizacao', 'delecao',
                    'ativo',
                    )
