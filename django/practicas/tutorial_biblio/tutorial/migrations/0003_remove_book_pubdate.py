# Generated by Django 2.1.1 on 2018-10-08 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_auto_20181008_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pubdate',
        ),
    ]
