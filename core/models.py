from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    descricao = models.CharField('Descrição', max_length=500)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    cidade = models.CharField('Cidade', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    endereco = models.CharField("Endereço", max_length=100)

