# Generated by Django 2.1.1 on 2018-10-08 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='num_awards',
        ),
    ]