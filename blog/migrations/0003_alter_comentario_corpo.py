# Generated by Django 5.0.3 on 2024-05-06 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contato_alter_imagem_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='corpo',
            field=models.CharField(max_length=500),
        ),
    ]