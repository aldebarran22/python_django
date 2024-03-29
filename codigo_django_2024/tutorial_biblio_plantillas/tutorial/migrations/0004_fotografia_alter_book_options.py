# Generated by Django 5.0.2 on 2024-02-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0003_remove_book_pubdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('fotografia', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['price']},
        ),
    ]
