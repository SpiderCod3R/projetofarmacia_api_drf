from djmoney.models.fields import MoneyField
from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    delecao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class TipoMedicamento(Base):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Tipo Medicamento'
        verbose_name_plural = 'Tipo Medicamentos'

    def __str__(self):
        return self.nome


class Laboratorio(Base):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Laboratório'
        verbose_name_plural = 'Laboratório'

    def __str__(self):
        return self.nome


class Medida(Base):
    medida = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'

    def __str__(self):
        return self.medida


class Medicamento(Base):
    titulo = models.CharField(max_length=255)
    descricao_medicamento = models.CharField(max_length=255)
    lote = models.CharField(max_length=55)
    validade = models.DateTimeField
    preco = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    medida = models.CharField(max_length=55)
    peso_liquido = models.CharField(max_length=55)
    tipo_medicamento = models.ForeignKey(TipoMedicamento, related_name='tipo_medicamentos', on_delete=models.CASCADE)
    tipo_uso = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, related_name='laboratorios', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        unique_together = ['titulo', 'laboratorio', 'lote']


