from django import forms

from .models import Bandeira, Checklist, Membro, Tarefa


class TarefaModelForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['name', 'responsavel', 'descricao',
                  'categoria', 'lista', 'dt_inicio', 'dt_final', ]


class MembroModelForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['membro_nome', ]


class BandeiraModelForm(forms.ModelForm):
    class Meta:
        model = Bandeira
        fields = ['name',]


class ChecklistModelForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['name',]
