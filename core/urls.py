from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, minhaconta, sobre, cupcakes, base, entrega, cadastro, minhaconta_logado, contato

urlpatterns = [
    path('', index, name='home'),
    path('base', base, name='base'),
    path('minhaconta', minhaconta, name='minhaconta'),
    path('sobre', sobre, name='sobre'),
    path('cupcakes', cupcakes, name='cupcakes'),
    path('entrega', entrega, name='entrega'),
    path('cadastro', cadastro, name='cadastro'),
    path('minhaconta_logado', minhaconta_logado, name='minhaconta_logado'),
    path('contato', contato, name='contato'),
    path('logout/', LogoutView.as_view(next_page='minhaconta'), name='logout'),

]
