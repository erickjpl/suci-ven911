# Generated by Django 4.2.7 on 2024-07-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uri', '0009_tipoaccidente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viajaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viajaba', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'viajaba',
                'verbose_name_plural': 'viajabas',
            },
        ),
    ]
