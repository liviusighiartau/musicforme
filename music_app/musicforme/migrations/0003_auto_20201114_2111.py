# Generated by Django 3.1.3 on 2020-11-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicforme', '0002_auto_20201114_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='headline',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
