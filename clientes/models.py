from django.db import models
from farmacia.abstract_models import Base


class Endereco(Base):
    endereco = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    UF = models.CharField(max_length=50)
    CEP = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['endereco']
        unique_together = ['endereco', 'CEP', 'numero']

    def endereco_completo(self):
        return f'{self.endereco}, {self.bairro} - {self.cep}'

    def cidade_estado(self):
        return f'{self.cidade}/{self.UF}'

    def __str__(self):
        return f'{self.endereco_completo()}, {self.cidade_estado()}'


class Cliente(Base):
    nome = models.CharField(max_length=50)
    dtaNascimento = models.DateField()
    CPF = models.CharField(max_length=14)
    RG = models.CharField(max_length=14, blank=True, default='')
    CEL = models.CharField(max_length=14, blank=True, default='')
    SEXO = models.CharField(max_length=10, blank=True, default='')
    email = models.EmailField(max_length=255, unique=True)
    enderecos = models.ManyToManyField(Endereco)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']
        unique_together = ['nome', 'CPF', 'RG']



