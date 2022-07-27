from django.contrib import admin
from medicamentos.models import TipoMedicamento, Laboratorio, Medida, Medicamento


@admin.register(TipoMedicamento)
class TipoMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'delecao', 'ativo')


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'delecao', 'ativo')


@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('medida', 'criacao', 'atualizacao', 'delecao', 'ativo')


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao_medicamento', 'lote', 'validade', 'preco', 'medida', 'peso_liquido',
                    'tipo_medicamento', 'tipo_uso', 'laboratorio', 'criacao','atualizacao', 'delecao', 'ativo')
