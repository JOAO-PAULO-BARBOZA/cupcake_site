from django.db import models
from django.contrib.auth.models import User


class DadosUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione outros campos conforme necessário
    endereco = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=55, blank=True, null=True)


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome







