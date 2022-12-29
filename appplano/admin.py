from django.contrib import admin

from .models import (Acao_Melhoria, Indicador_Estrategico, Item_Plano_Acao,
                     Perspectiva, Pilar, Plano_Acao, Ponto_Critico,
                     Unidade_Negocio)


@admin.register(Pilar)
class PilarAdmin(admin.ModelAdmin):
    list_display = ['nome', ]


@admin.register(Unidade_Negocio)
class Unidade_NegocioAdmin(admin.ModelAdmin):
    list_display = ['nome', ]


@admin.register(Perspectiva)
class PerspectivaAdmin(admin.ModelAdmin):
    list_display = ['nome', ]


@admin.register(Indicador_Estrategico)
class Indicador_EstrategicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'objetivo_estrategico', 'instituicao', ]


class Item_Plano_AcaoInline(admin.TabularInline):
    model = Item_Plano_Acao
    extra = 1


@admin.register(Plano_Acao)
class PlanoAcaoAdmin(admin.ModelAdmin):
    inlines = [
        Item_Plano_AcaoInline
    ]


class Acao_MelhoriaInline(admin.TabularInline):
    model = Acao_Melhoria
    extra = 1


@admin.register(Ponto_Critico)
class Ponto_CriticoAdmin(admin.ModelAdmin):
    inlines = [
        Acao_MelhoriaInline
    ]
