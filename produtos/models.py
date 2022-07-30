from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    delecao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class TipoProduto(Base):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Tipo Produto'
        verbose_name_plural = 'Tipo Produtos'

    def __str__(self):
        return self.nome


class TipoDeUso(Base):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Tipo de Uso'
        verbose_name_plural = 'Tipos de Uso'

    def __str__(self):
        return self.nome


class Medida(Base):
    medida = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'

    def __str__(self):
        return self.medida


class Fabricante(Base):
    nome = models.CharField(max_length=255)
    CNPJ = models.CharField(max_length=14, blank=True, default='')
    telefone1 = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True)
    site_url = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricante'
        unique_together = ['nome', 'CNPJ']

    def __str__(self):
        return self.nome


class Fornecedor(Base):
    nome = models.CharField(max_length=255)
    CNPJ = models.CharField(max_length=14, blank=True, default='')
    telefone1 = models.CharField(max_length=15)
    telefone2 = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField(max_length=255, unique=True)
    site_url = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        unique_together = ['nome', 'CNPJ']

    def __str__(self):
        return f'{self.nome} - [{self.CNPJ}]'


class Produto(Base):
    nome = models.CharField(max_length=255)
    descricao_produto = models.TextField(max_length=500, blank=True, default='')
    lote = models.CharField(max_length=55)
    quantidade = models.IntegerField()
    validade = models.DateTimeField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    medida = models.ForeignKey(Medida, related_name='medidas', blank=True, default='', on_delete=models.CASCADE)
    peso_liquido = models.CharField(max_length=55, blank=True, default='')
    tipo_produto = models.ForeignKey(TipoProduto, related_name='tipo_produtos', on_delete=models.CASCADE)
    tipo_uso = models.ForeignKey(TipoDeUso, related_name='tipos_de_uso', on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, related_name='fabricantes', on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, related_name='fornecedores', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        unique_together = ['nome', 'fabricante', 'lote']

    def __str__(self):
        return f'{self.nome} - {self.lote} - [{self.quantidade}]'
