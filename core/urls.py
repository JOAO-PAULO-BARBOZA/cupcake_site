from django.urls import path
from .views import index, minhaconta, sobre, cupcakes, base, entrega, cadastro

urlpatterns = [
    path('', index, name='home'),
    path('base', base, name='base'),
    path('minhaconta', minhaconta, name='minhaconta'),
    path('sobre', sobre, name='sobre'),
    path('cupcakes', cupcakes, name='cupcakes'),
    path('entrega', entrega, name='entrega'),
    path('cadastro', cadastro, name='cadastro'),

]
