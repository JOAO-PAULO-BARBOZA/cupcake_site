from django import forms
from django.core.mail.message import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Menssagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        mail = EmailMessage(
            subject= assunto,
            body= conteudo,
            from_email= 'contato@seudominio.com.br',
            to= ['contato@seudominio.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Nome")
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Sobrenome")
    email = forms.EmailField(
        max_length=254,
        required=True,)
    username = forms.CharField(
        label='Usuário',
        max_length=150,
        required=True,
        help_text=''
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput,
        help_text=''
    )
    password2 = forms.CharField(
        label='Confirmar',
        widget=forms.PasswordInput,
        help_text=' '
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Digite seu nome'})

        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Digite seu sobrenome',
             'style': 'margin-left: 20px',})

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Informe um email válido'})

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Digite seu nome de usuário',
             'style': 'margin-left: 45px'
             })

        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Digite sua senha',
             'style': 'margin-left: 55px',
             })

        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Confirme sua senha',
             'style': 'margin-left: 30px',
             })


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)