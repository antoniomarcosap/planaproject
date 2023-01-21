from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
        }),
        label='Senha',
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Redigite sua senha',
        }),
        label='Confirmar Senha',
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

        labels = {
            'username': 'Nome de Usuário',
            'email': 'Email',
        }

        error_messages = {
            'username': {
                'required': 'Este campo é obrigatório',
            },
            'email': {
                'required': 'Este campo é obrigatório',
            }
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Ex.: nome.sobrenome',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ex.: usuario@email.com',
            }),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        exists = User.objects.filter(username=username).exists()
        if exists:
            raise ValidationError(
                'Já existe um cadastro com este usuário no sistema',
                code='invalid',)
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise ValidationError(
                'Já existe uma conta com este email no sistema',
                code='invalid',)
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(
                'As senhas digitadas não são iguais.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'email',
        )

        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome Completo',
            'email': 'Email',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'data_nascimento',
            'foto',
        )

        labels = {
            'data_nascimento': 'Data de Nascimento',
            'foto': 'Foto',
        }
