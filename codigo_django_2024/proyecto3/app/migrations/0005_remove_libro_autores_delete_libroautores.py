# Generated by Django 5.0.2 on 2024-02-21 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_libroautores_alter_libro_autores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autores',
        ),
        migrations.DeleteModel(
            name='LibroAutores',
        ),
    ]