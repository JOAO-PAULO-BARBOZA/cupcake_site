from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm


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
    return render(request, 'cupcakes.html')


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





