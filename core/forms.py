from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome")
    email = forms.EmailField(label="E-mail")
    cidade = forms.CharField(label="Cidade")
    bairro = forms.CharField(label="Bairro")
    endereco = forms.CharField(label="Endereço")


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150, required=True, label='E-mail')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Senha')


