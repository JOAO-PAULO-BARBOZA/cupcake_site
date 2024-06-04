from django.db import models
from django.contrib.auth.models import User


class DadosUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione outros campos conforme necessário
    endereco = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=55, blank=True, null=True)






