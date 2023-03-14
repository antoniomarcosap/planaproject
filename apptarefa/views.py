from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView

from . import models
from .forms import (BandeiraModelForm, ChecklistModelForm, MembroModelForm,
                    TarefaModelForm)
from .models import Bandeira, Checklist, Membro, Tarefa


class TaskList(LoginRequiredMixin, ListView):
    model = models.Tarefa
    template_name = 'apptarefa/tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tarefa.objects.filter(responsavel=self.request.user).order_by('-dt_criacao')
