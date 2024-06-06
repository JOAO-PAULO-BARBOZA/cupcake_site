from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('base', views.base, name='base'),
    path('minhaconta', views.minhaconta, name='minhaconta'),
    path('sobre', views.sobre, name='sobre'),
    path('cupcakes', views.cupcakes, name='cupcakes'),
    path('entrega', views.entrega, name='entrega'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('minhaconta_logado', views.minhaconta_logado, name='minhaconta_logado'),
    path('contato', views.contato, name='contato'),
    path('logout/', LogoutView.as_view(next_page='minhaconta'), name='logout'),
    path('produtos/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
    path('carrinho/', views.exibir_carrinho, name='exibir_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/atualizar/', views.atualizar_item_carrinho, name='atualizar_item_carrinho'),
    path('carrinho/excluir/<int:item_id>', views.excluir_item_carrinho, name='excluir_item_carrinho'),
    path('carrinho/excluir_todos', views.excluir_todos_itens_carrinho, name='excluir_todos_itens_carrinho'),
    path('carrinho/checkout', views.checkout, name='checkout'),
    path('pedido_confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
    path('pedido_confirmado/<str:metodo_pagamento>/', views.pedido_confirmado, name='pedido_confirmado'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


