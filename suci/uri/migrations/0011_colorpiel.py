# Generated by Django 4.2.7 on 2024-07-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uri', '0010_viajaba'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorPiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_piel', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'color_piel',
                'verbose_name_plural': 'color_pieles',
            },
        ),
    ]