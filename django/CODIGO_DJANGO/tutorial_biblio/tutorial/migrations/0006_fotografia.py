# Generated by Django 4.2.3 on 2023-08-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0005_alter_book_options_book_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, null=True)),
                ('foto', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
