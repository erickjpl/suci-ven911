# Generated by Django 5.0.3 on 2024-04-04 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0004_particular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambulancia',
            name='transporte',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='transporte',
        ),
        migrations.RemoveField(
            model_name='patrulla',
            name='transporte',
        ),
    ]
