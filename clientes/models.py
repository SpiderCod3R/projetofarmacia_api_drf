from django.db import models
from farmacia_enderecos.models import Endereco
from farmacia.abstract_models import Base


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



