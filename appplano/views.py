# from django.shortcuts import render
from django.urls import reverse
from extra_views import (CreateWithInlinesView, InlineFormSetFactory,
                         UpdateWithInlinesView)

from .models import Item_Plano_Acao, Plano_Acao


class ItemInline(InlineFormSetFactory):
    model = Item_Plano_Acao
    fields = ['nome', 'como', 'quem', 'data_inicio',
              'data_fim', 'quanto', 'risco_estrategia',
              'evidencia', 'arquivo_evidencia', 'status',]
    factory_kwargs = {
        'extra': 1,
        'max_num': None,
        'can_order': False,
        'can_delete': True,
    }


class PlanoCreateView(CreateWithInlinesView):
    model = Plano_Acao
    inlines = [ItemInline]
    fields = ['nome', 'responsavel_plano',
              'indicador_estrategico', 'pilar',
              'unidade_negocio', 'perspectiva',]
    template_name = 'appplano/plano_create.html'

    def get_success_url(self):
        return reverse('plano:planocreate')


class PlanoUpdateView(UpdateWithInlinesView):
    model = Plano_Acao
    inlines = [ItemInline]
    fields = ['nome', 'responsavel_plano',
              'indicador_estrategico', 'pilar',
              'unidade_negocio', 'perspectiva',]
    template_name = 'appplano/plano_create.html'

    def get_success_url(self):
        return reverse('plano:planocreate')
