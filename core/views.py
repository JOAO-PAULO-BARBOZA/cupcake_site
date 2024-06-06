from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm, ContatoForm, CheckoutForm, ItemCarrinhoForm
from .models import Produto, Carrinho, ItemCarrinho, ItemPedido, Pedido
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, template_name='base.html')


def minhaconta(request):
    if request.user.is_authenticated:
        return redirect('minhaconta_logado')

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecionar para a página após o login bem-sucedido
                return redirect('minhaconta_logado')  # Altere para a página desejada
    else:
        form = LoginForm()
        return render(request, 'minhaconta.html', {'form': form})


def cupcakes(request):
    produtos = Produto.objects.all()
    categoria = request.GET.get('categoria')
    decoracao = request.GET.get('decoracao')
    sabor = request.GET.get('sabor')

    if categoria:
        produtos = produtos.filter(categoria=categoria)
    if decoracao:
        produtos = produtos.filter(decoracao=decoracao)
    if sabor:
        produtos = produtos.filter(sabor=sabor)

    context = {
        'produtos': produtos,
    }
    return render(request, 'cupcakes.html', context)


def sobre(request):
    return render(request, 'sobre.html')


def entrega(request):
    return render(request, 'entrega.html')


def cadastro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirecionar para a página inicial após o login
    else:
        form = RegisterForm()
    return render(request, 'cadastro.html', {'form': form})


def minhaconta_logado(request):
    return render(request, 'minhaconta_logado.html')


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Mensagem enviada com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar Mensagem')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

# REVER CÓDIGO DAQUI


def lista_produtos(request):
    produtos = Produto.objects.all()
    categoria = request.GET.get('categoria')
    decoracao = request.GET.get('decoracao')
    sabor = request.GET.get('sabor')

    if categoria:
        produtos = produtos.filter(categoria=categoria)
    if decoracao:
        produtos = produtos.filter(decoracao=decoracao)
    if sabor:
        produtos = produtos.filter(sabor=sabor)

    context = {
        'produtos': produtos,
    }
    return render(request, 'lista_produtos.html', context)


def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})


@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)
    item, item_criado = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
        defaults={
            'quantidade': 1,
            'decoracao': request.POST.get('decoracao', 'simples'),
            'cobertura': request.POST.get('cobertura', 'creme_chocolate')
        }
    )
    if not item_criado:
        item.quantidade += 1
        item.save()

    return redirect('cupcakes')


def exibir_carrinho(request):
    carrinho = Carrinho.objects.get(usuario=request.user)
    itens = carrinho.itens.all()
    return render(request, 'carrinho/exibir_carrinho.html', {'carrinho': carrinho, 'itens': itens})


@login_required
def atualizar_item_carrinho(request):
    carrinho = Carrinho.objects.get(usuario=request.user)
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)

    if request.method == 'POST':
        for item in itens:
            form = ItemCarrinhoForm(request.POST, instance=item)
            if form.is_valid():
                form.save()

        # Redirecionar para a mesma página para exibir as atualizações
        return HttpResponseRedirect(request.path_info)

    forms = [ItemCarrinhoForm(instance=item) for item in itens]
    context = {
        'carrinho': carrinho,
        'itens_forms': forms,
    }
    return render(request, 'carrinho/atualizar_item_carrinho.html', context)


def excluir_item_carrinho(request, item_id):
    # Sua lógica para excluir o item do carrinho com o ID fornecido
    item = ItemCarrinho.objects.get(id=item_id)
    item.delete()
    return redirect('exibir_carrinho')


def excluir_todos_itens_carrinho(request):
    # Sua lógica para excluir todos os itens do carrinho
    ItemCarrinho.objects.all().delete()
    return redirect('exibir_carrinho')


@login_required
def checkout(request):
    usuario = request.user
    carrinho = Carrinho.objects.get(usuario=usuario)
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)
    total = sum(item.preco_total for item in itens)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            metodo_pagamento = form.cleaned_data['metodo_pagamento']
            # Criar o pedido
            pedido = Pedido.objects.create(
                usuario=usuario,
                total=total
            )
            for item in itens:
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=item.produto,
                    quantidade=item.quantidade,
                    decoracao=item.decoracao,
                    cobertura=item.cobertura,
                    preco_total=item.preco_total
                )
            # Limpar o carrinho
            itens.delete()

            # Redirecionar para a página de confirmação com o método de pagamento escolhido
            return redirect('pedido_confirmado', metodo_pagamento=metodo_pagamento)
    else:
        form = CheckoutForm()

    context = {
        'carrinho': carrinho,
        'itens': itens,
        'total': total,
        'form': form
    }
    return render(request, 'carrinho/checkout.html', context)


def pedido_confirmado(request, metodo_pagamento):
    context = {
        'metodo_pagamento': metodo_pagamento,
    }
    return render(request, 'pedido_confirmado.html', context)

