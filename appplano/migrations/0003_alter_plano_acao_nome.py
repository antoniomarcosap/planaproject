# Generated by Django 3.2 on 2023-03-07 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appplano', '0002_alter_item_plano_acao_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano_acao',
            name='nome',
            field=models.TextField(db_index=True, default='', max_length=255, verbose_name='Linha de Ação'),
        ),
    ]
