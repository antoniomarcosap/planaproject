from django.contrib import admin

from .models import Bandeira, Categoria, Checklist, Lista, Membro, Tarefa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display = ['name',]


class BandeiraInline(admin.TabularInline):
    model = Bandeira
    extra = 1


class ChecklistInline(admin.TabularInline):
    model = Checklist
    extra = 1


class MembroInline(admin.TabularInline):
    model = Membro
    extra = 1


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    inlines = [
        BandeiraInline,
        ChecklistInline,
        MembroInline,
    ]
