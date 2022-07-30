from django.contrib import admin
from produtos.models import TipoProduto, TipoDeUso, Fornecedor, Medida, Produto, Fabricante


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lote', 'quantidade',
                    'validade', 'descricao_produto', 'preco',
                    'medida',
                    'peso_liquido',
                    'tipo_produto',
                    'tipo_uso',
                    'fabricante',
                    'fornecedor',
                    'criacao', 'atualizacao', 'delecao',
                    'ativo',
                    )
    icon_name = 'dvr'


@admin.register(TipoProduto)
class TipoProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo')


@admin.register(TipoDeUso)
class TipoDeUsoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'delecao', 'ativo')


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'CNPJ', 'telefone1', 'telefone2', 'criacao', 'atualizacao', 'delecao', 'ativo')
    icon_name = "class"


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'CNPJ', 'telefone1', 'telefone2', 'criacao', 'atualizacao', 'delecao', 'ativo')
    icon_name = "class"


@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('medida', 'criacao', 'atualizacao', 'delecao', 'ativo')


