# Generated by Django 4.2 on 2023-04-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0009_registro_financeiro_vencimento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_financeiro',
            name='parcela',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='registro_financeiro',
            name='total_parcela',
            field=models.IntegerField(default=1),
        ),
    ]