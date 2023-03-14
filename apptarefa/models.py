from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# ADICIONAR RELEVÂNCIA E URGÊNCIA


class Categoria(models.Model):
    name = models.CharField(
        max_length=50,
        db_index=True,
        default='',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Lista(models.Model):
    name = models.CharField(
        max_length=50,
        db_index=True,
        default='',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'

    def __str__(self):
        return self.name


class Tarefa(models.Model):
    name = models.CharField(
        default='',
        db_index=True,
        max_length=255,
        null=False,
    )

    responsavel = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=60,
        db_index=True,
        default='',
        verbose_name='Responsável',
    )

    descricao = models.TextField(
        max_length=255,
        db_index=True,
        verbose_name='Descrição',
        null=True,
    )

    categoria = models.ForeignKey(
        Categoria,
        related_name='tarefa_categoria',
        on_delete=models.DO_NOTHING,
        verbose_name='Categoria',
        null=False,
    )

    lista = models.ForeignKey(
        Lista,
        related_name='tarefa_lista',
        on_delete=models.DO_NOTHING,
        verbose_name='Lista',
        null=False,
    )

    dt_inicio = models.DateField(
        default=timezone.now,
        verbose_name='Data de Início',
    )

    dt_final = models.DateField(
        default=timezone.now,
        verbose_name='Data de Finalização',
    )

    dt_criacao = models.DateTimeField(
        auto_now_add=True,
    )

    dt_atualizacao = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.name


class Membro(models.Model):
    tarefa = models.ForeignKey(
        Tarefa,
        related_name='membro_tarefa',
        on_delete=models.DO_NOTHING,
    )

    membro_nome = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=60,
        db_index=True,
        default='',
        verbose_name='Membro',
    )

    class Meta:
        ordering = ('membro_nome',)
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def __str__(self):
        return self.membro_nome


class Bandeira(models.Model):
    tarefa = models.ForeignKey(
        Tarefa,
        related_name='bandeira_tarefa',
        on_delete=models.DO_NOTHING,
    )

    name = models.CharField(
        max_length=100,
        default='',
        db_index=True,
        verbose_name='Nome',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Bandeira'
        verbose_name_plural = 'Bandeiras'

    def __str__(self):
        return self.name


class Checklist(models.Model):
    tarefa = models.ForeignKey(
        Tarefa,
        related_name='checklist_tarefa',
        on_delete=models.DO_NOTHING,
    )

    name = models.CharField(
        default='',
        max_length=255,
        db_index=True,
        verbose_name='Nome',
    )

    completo = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ('completo',)
        verbose_name = 'Checklist'

    def __str__(self):
        return self.completo
