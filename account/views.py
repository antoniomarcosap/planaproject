from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import LoginForm, ProfileEditForm, RegisterForm, UserEditForm
from .models import Profile


class HomeView(TemplateView):
    template_name = 'account/home.html'


@login_required
def DashboardView(request):
    return render(request, 'account/dashboard.html')


def LoginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/dashboard.html')
                else:
                    return HttpResponse('Conta Inativa')
            else:
                messages.info(
                    request, 'Login Inválido. Você ainda tem duas tentativas')
                return render(request, 'account/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def RegisterView(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(
                request, 'Seu pedido de cadastro foi enviado. Aguarde o email de confirmação')
            return render(request, 'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = RegisterForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def UserEditView(request):
    if request.method == "POST":
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Seu perfil foi atualizado.')
        else:
            messages.error(
                request, 'Ops! :| Não foi possível atualizar o seu perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/profile_edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def PasswordChangeView(request):
    return render(request, 'account/password_change.html')
