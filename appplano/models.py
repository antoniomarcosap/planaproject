from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Pilar(models.Model):
    nome = models.CharField(
        max_length=50,
        db_index=True,
        default='',
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Pilar'
        verbose_name_plural = 'Pilares'

    def __str__(self):
        return self.nome


class Unidade_Negocio(models.Model):
    nome = models.CharField(
        max_length=50,
        db_index=True,
        default='',
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Unidade de Negócio'
        verbose_name_plural = 'Unidades de Negócios'

    def __str__(self):
        return self.nome


class Perspectiva(models.Model):
    nome = models.CharField(
        max_length=50,
        db_index=True,
        default='',
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Perspectiva'
        verbose_name_plural = 'Perspectivas'

    def __str__(self):
        return self.nome


class Indicador_Estrategico(models.Model):
    EMPRESA = (
        ('Sesi', 'SESI'),
        ('Senai', 'SENAI'),
    )

    nome = models.CharField(
        max_length=150,
        db_index=True,
        default='',
        verbose_name='Indicador'
    )

    instituicao = models.CharField(
        max_length=11,
        choices=EMPRESA,
        default='SENAI',
    )

    objetivo_estrategico = models.CharField(
        max_length=150,
        db_index=True,
        default='',
        verbose_name='Objetivo Estratégico'
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Indicador Estratégico'
        verbose_name_plural = 'Indicadores Estratégicos'

    def __str__(self):
        return self.nome


class Plano_Acao(models.Model):
    responsavel_plano = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=60,
        db_index=True,
        default='',
        verbose_name='Responsável pelo Plano'
    )

    nome = models.CharField(
        max_length=150,
        db_index=True,
        default='',
        verbose_name='Linha de Ação'
    )

    indicador_estrategico = models.ForeignKey(
        Indicador_Estrategico,
        related_name='plano_indicador',
        on_delete=models.DO_NOTHING,
        verbose_name='Indicador Estratégico'
    )

    pilar = models.ForeignKey(
        Pilar,
        related_name='plano_pilar',
        on_delete=models.DO_NOTHING,
        verbose_name='Pilar',
    )

    unidade_negocio = models.ForeignKey(
        Unidade_Negocio,
        related_name='plano_unidade',
        on_delete=models.DO_NOTHING,
        verbose_name='Unidade de Negócio'
    )

    perspectiva = models.ForeignKey(
        Perspectiva,
        related_name='plano_perspectiva',
        on_delete=models.DO_NOTHING,
    )

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Plano de ação'
        verbose_name_plural = 'Planos de Ações'

    def __str__(self):
        return self.nome


class Item_Plano_Acao(models.Model):
    STATUS = (
        ('Planejado', 'Planejado'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
        ('Atrasado', 'Atrasado'),
    )

    EVIDENCIA = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )

    plano_acao = models.ForeignKey(
        Plano_Acao,
        related_name='item_plano',
        on_delete=models.CASCADE,
    )

    nome = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name='O que?',
    )

    como = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name='Como?',
    )

    quem = models.CharField(
        max_length=140,
        db_index=True,
        verbose_name='Quem?',
    )

    data_inicio = models.DateField(
        default=timezone.now,
        verbose_name='Data de Início',
    )

    data_fim = models.DateField(
        default=timezone.now,
        verbose_name='Data de Finalização',
    )

    onde = models.CharField(
        max_length=140,
        db_index=True,
        verbose_name='Onde?',
    )

    porque = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name='Por que?',
    )

    quanto = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Quanto?',
    )

    risco_estrategia = models.CharField(
        max_length=140,
        db_index=True,
        verbose_name='Risco à Estratégia',
    )

    evidencia = models.CharField(
        max_length=4,
        choices=EVIDENCIA,
        default='Não',
    )

    arquivo_evidencia = models.FileField(
        upload_to='arquivos_evidencias',
        blank=True,
    )

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=12,
        choices=STATUS,
        default='Planejado',
    )

    class Meta:
        ordering = ('id',)
        index_together = (('id',))
        verbose_name = 'Item do Plano de Ação'
        verbose_name_plural = 'Itens do Plano'

    def __str__(self):
        return self.nome


class Ponto_Critico(models.Model):
    nome = models.CharField(
        max_length=255,
        db_index=True,
        default='',
        verbose_name='Descrição'
    )

    plano_acao = models.ForeignKey(
        Plano_Acao,
        related_name='ponto_plano',
        on_delete=models.CASCADE,
        verbose_name='Plano de Ação'
    )

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Ponto Crítico'
        verbose_name_plural = 'Pontos Críticos'

    def __str__(self):
        return self.nome


class Acao_Melhoria(models.Model):
    STATUS = (
        ('Planejado', 'Planejado'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
        ('Atrasado', 'Atrasado'),
    )

    EVIDENCIA = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )

    nome = models.CharField(
        max_length=150,
        db_index=True,
        default='',
        verbose_name='Ação de Melhoria'
    )

    ponto_critico = models.ForeignKey(
        Ponto_Critico,
        related_name='acao_ponto',
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=12,
        choices=STATUS,
        default='Planejado',
        verbose_name='Status'
    )

    evidencia = models.CharField(
        max_length=4,
        choices=EVIDENCIA,
        default='Não',
        verbose_name='Evidência?'
    )

    arquivo_evidencia = models.FileField(
        upload_to='arquivos_evidencias',
        blank=True,
        verbose_name='Arquivo de Evidência'
    )

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Ação de Melhoria'
        verbose_name_plural = 'Ações de Melhorias'

    def __str__(self):
        return self.nome
