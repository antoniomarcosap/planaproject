from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView

from . import models
from .forms import Item_Plano_AcaoModelForm, PlanoModelForm
from .models import Item_Plano_Acao, Plano_Acao


class ListaPlanos(LoginRequiredMixin, ListView):
    model = models.Plano_Acao
    template_name = 'appplano/plano_list.html'
    context_object_name = 'plano'

    def get_queryset(self):
        return Plano_Acao.objects.filter(responsavel_plano=self.request.user).order_by('-criacao')


class DetalhePlano(LoginRequiredMixin, DetailView):
    model = models.Plano_Acao
    queryset = Plano_Acao.objects.all()
    template_name = 'appplano/plano_detail.html'
    context_object_name = 'plano'


@ login_required
def AdicionarPlano(request):
    if request.method == "GET":
        planform = PlanoModelForm()
        form_item_factory = inlineformset_factory(
            Plano_Acao, Item_Plano_Acao, form=Item_Plano_AcaoModelForm, extra=0
        )
        form_item = form_item_factory()
        context = {
            'planform': planform,
            'form_item': form_item,
        }
        return render(request, 'appplano/plano_create.html', context)
    elif request.method == "POST":
        planform = PlanoModelForm(request.POST)
        form_item_factory = inlineformset_factory(
            Plano_Acao, Item_Plano_Acao, form=Item_Plano_AcaoModelForm
        )
        form_item = form_item_factory(request.POST)
        if planform.is_valid() and form_item.is_valid():
            addplano = planform.save()
            form_item.instance = addplano
            form_item.save()
            return redirect(reverse('plano:planlist'))
        else:
            context = {
                'planform': planform,
                'form_item': form_item,
            }
            return render(request, 'appplano/plano_create.html', context)


@login_required
def AtualizarPlano(request, pk):
    if request.method == "GET":
        planoject = Plano_Acao.objects.filter(id=pk).first()
        if planoject is None:
            return redirect(reverse('plano:planlist'))
        planform = PlanoModelForm(instance=planoject)
        form_item_factory = inlineformset_factory(
            Plano_Acao, Item_Plano_Acao, form=Item_Plano_AcaoModelForm, extra=0
        )
        form_item = form_item_factory(instance=planoject)
        context = {
            'planform': planform,
            'form_item': form_item,
        }
        return render(request, 'appplano/plano_create.html', context)

    elif request.method == "POST":
        planoject = Plano_Acao.objects.filter(id=pk).first()
        if planoject is None:
            return redirect(reverse('plano:planlist'))
        planform = PlanoModelForm(request.POST, instance=planoject)
        form_item_factory = inlineformset_factory(
            Plano_Acao, Item_Plano_Acao, form=Item_Plano_AcaoModelForm
        )
        form_item = form_item_factory(request.POST, instance=planoject)
        if planform.is_valid() and form_item.is_valid():
            addplano = planform.save()
            form_item.instance = addplano
            form_item.save()
            return redirect(reverse('plano:planlist'))
        else:
            context = {
                'planform': planform,
                'form_item': form_item,
            }
            return render(request, 'appplano/plano_create.html', context)


class RemoverPlano(LoginRequiredMixin, DeleteView):
    queryset = Plano_Acao.objects.all()
    template_name = 'appplano/plan_confirm_delete.html'
    success_url = reverse_lazy('plano:planlist')
