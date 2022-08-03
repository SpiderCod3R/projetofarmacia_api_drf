from django.contrib import admin

from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dtaNascimento', 'CPF',
                    'RG', 'CEL', 'SEXO', 'email',
                    'criacao', 'atualizacao', 'delecao',
                    'ativo',
                    )