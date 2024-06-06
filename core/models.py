from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from stdimage import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils import timezone


class DadosUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione outros campos conforme necessário
    endereco = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=55, blank=True, null=True)


class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', default=timezone.now)
    modificado = models.DateTimeField('Data de Modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    CATEGORIA_CHOICES = [
        ('tradicional', 'Tradicional'),
        ('vegano', 'Vegano'),
        ('sem_glutem', 'Sem Glúten'),
    ]

    DECORACAO_CHOICES = [
        ('simples', 'Simples'),
        ('elaborada', 'Elaborada'),
    ]

    SABOR_CHOICES = [
        ('chocolate', 'Chocolate'),
        ('morango', 'Morango'),
        ('baunilha', 'Baunilha'),
        ('maracuja', 'Maracujá'),
        ('coco', 'Coco'),
        ('limao', 'Limão'),
        ('cenoura', 'Cenoura')
    ]

    COBERTURA_CHOICES = [
        ('creme_chocolate', 'Creme de Chocolate'),
        ('creme_morango', 'Creme de Morango'),
        ('creme_baunilha', 'Creme de Baunilha'),
        ('creme_maracuja', 'Creme de Maracujá'),
        ('raspa_coco', 'Raspa de Coco'),
        ('raspa_limao', 'Raspa de Limão'),
        ('buttercream', 'Buttercream'),
        ('chantilly.', 'Chantilly'),
        ('merengue', 'Merengue'),
        ('nozes', 'Nozes')

    ]

    nome = models.CharField( verbose_name='Nome',max_length=100)
    descricao = models.TextField(verbose_name= 'Descrição', max_length=240)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    imagem = StdImageField(
        'Imagem',
        upload_to='produtos/',
        variations={'thumb': (150, 150, True),'medium': (300, 300, True), 'large': (600, 600, True),
        }
    )
    estoque = models.PositiveIntegerField('Estoque', default=500)
    categoria = models.CharField('Categoria', max_length=20, choices=CATEGORIA_CHOICES, default='Tradicional')
    decoracao = models.CharField('Decoração', max_length=20, choices=DECORACAO_CHOICES, default='Simples')
    sabor = models.CharField('Sabor', max_length=20, choices=SABOR_CHOICES, default='Chocolate')
    cobertura = models.CharField('Cobertura', max_length=20, choices=COBERTURA_CHOICES, default='Creme de Chocolate')

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, Produto)


class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateTimeField('Data de Criação', default=timezone.now)
    modificado = models.DateTimeField('Data de Modificação', auto_now=True)

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens', default=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    decoracao = models.CharField(max_length=20, choices=Produto.DECORACAO_CHOICES, default='simples')
    cobertura = models.CharField(max_length=20, choices=Produto.COBERTURA_CHOICES, default='creme_chocolate')

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'

    @property
    def preco_total(self):
        preco = float(self.produto.preco) * float(self.quantidade)
        if self.decoracao == 'elaborada':
            preco += 0.1 * float(self.produto.preco) * float(self.quantidade)
        return round(preco, 2)


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateTimeField('Data de Criação', default=timezone.now)
    modificado = models.DateTimeField('Data de Modificação', auto_now=True)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id} de {self.usuario.username}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    decoracao = models.CharField(max_length=20, choices=Produto.DECORACAO_CHOICES, default='simples')
    cobertura = models.CharField(max_length=20, choices=Produto.COBERTURA_CHOICES, default='creme_chocolate')
    preco_total = models.DecimalField('Preço Total', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'











