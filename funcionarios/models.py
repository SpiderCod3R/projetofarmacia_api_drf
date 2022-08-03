from django.db import models
from farmacia_enderecos.models import Endereco
from farmacia.abstract_models import Base
from django.utils.translation import  gettext_lazy as _


class Funcionario(Base):
    nome = models.CharField(_('Nome'), max_length=50)
    dtaNascimento = models.DateField(_('Data de Nascimento'))
    CPF = models.CharField(max_length=14)
    RG = models.CharField(max_length=14, blank=True, default='')
    CEL = models.CharField(max_length=14, blank=True, default='')
    SEXO = models.CharField(max_length=10, blank=True, default='')
    email = models.EmailField(_max_length=255, unique=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
        ordering = ['nome']
        unique_together = ['nome', 'CPF', 'RG', 'CEL', 'email']
