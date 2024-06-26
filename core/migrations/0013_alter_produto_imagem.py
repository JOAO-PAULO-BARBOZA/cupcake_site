# Generated by Django 4.1.7 on 2024-06-06 01:38

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_alter_produto_cobertura_alter_produto_sabor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="imagem",
            field=stdimage.models.StdImageField(
                force_min_size=False,
                upload_to="produtos/",
                variations={
                    "large": (600, 600, True),
                    "medium": (300, 300, True),
                    "thumb": (150, 150, True),
                },
                verbose_name="Imagem",
            ),
        ),
    ]
