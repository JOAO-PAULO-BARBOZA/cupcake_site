from django.contrib import admin
from .models import Produto, Carrinho, ItemCarrinho


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'preco', 'estoque', 'criado', 'modificado',
                    'ativo', 'categoria', 'decoracao', 'sabor', 'cobertura', 'imagem',)
    list_filter = ('categoria', 'decoracao', 'sabor', 'cobertura', 'ativo', 'criado', 'modificado')
    search_fields = ('nome', 'categoria', 'decoracao', 'sabor', 'cobertura')
    list_editable = ('categoria', 'decoracao', 'cobertura', 'preco', 'estoque', 'ativo', 'imagem',)


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'criado', 'modificado')


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'carrinho', 'produto', 'quantidade', 'decoracao', 'cobertura')
