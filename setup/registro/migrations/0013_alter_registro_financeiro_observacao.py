# Generated by Django 4.2 on 2023-04-26 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0012_alter_registro_financeiro_origem_debito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_financeiro',
            name='observacao',
            field=models.TextField(blank=True, default=''),
        ),
    ]
