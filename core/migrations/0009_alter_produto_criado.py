# Generated by Django 4.1.7 on 2024-06-05 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_produto_cobertura_produto_sabor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="criado",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Data de Criação"
            ),
        ),
    ]
