# Generated by Django 5.0.3 on 2024-04-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paneluser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='estado',
            field=models.CharField(default='', max_length=200, verbose_name='Estado:'),
        ),
    ]
