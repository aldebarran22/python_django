# Generated by Django 4.2.4 on 2023-08-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido1', models.CharField(max_length=30)),
                ('apellido2', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]