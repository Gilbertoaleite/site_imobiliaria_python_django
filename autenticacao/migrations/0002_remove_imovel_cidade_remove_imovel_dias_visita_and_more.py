# Generated by Django 4.0.1 on 2022-01-22 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='dias_visita',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='horarios',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='imagens',
        ),
        migrations.RemoveField(
            model_name='visitas',
            name='imovel',
        ),
        migrations.RemoveField(
            model_name='visitas',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.DeleteModel(
            name='DiasVisita',
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
        migrations.DeleteModel(
            name='imovel',
        ),
        migrations.DeleteModel(
            name='Visitas',
        ),
    ]
