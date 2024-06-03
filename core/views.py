from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import ContatoForm


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, template_name='base.html')


def minhaconta(request):
    form = ContatoForm()
    context = {

        "register_form": form
    }
    return render(request, 'minhaconta.html', context)


def cupcakes(request):
    return render(request, 'cupcakes.html')


def sobre(request):
    return render(request, 'sobre.html')


def entrega(request):
    return render(request, 'entrega.html')


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha_confirm = request.POST['confirmar']

        if senha == senha_confirm:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email já está em uso.')
            else:
                user = User.objects.create_user(username=email, email=email, password=senha)
                user.first_name = nome
                user.last_name = sobrenome
                user.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'As senhas não correspondem.')

    return render(request, template_name='cadastro.html')