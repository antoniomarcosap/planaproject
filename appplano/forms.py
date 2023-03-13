from django import forms

from .models import Item_Plano_Acao, Plano_Acao


class PlanoModelForm(forms.ModelForm):
    class Meta:
        model = Plano_Acao
        fields = ['nome', 'responsavel_plano', 'indicador_estrategico',
                  'pilar', 'unidade_negocio', 'perspectiva', ]


class Item_Plano_AcaoModelForm(forms.ModelForm):
    class Meta:
        model = Item_Plano_Acao
        fields = ['nome', 'como', 'quem',
                  'data_inicio', 'data_fim', 'onde',
                  'porque', 'quanto', 'risco_estrategia',
                  'evidencia', 'arquivo_evidencia', 'status', ]
