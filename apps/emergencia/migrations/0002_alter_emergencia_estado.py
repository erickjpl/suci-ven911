# Generated by Django 5.1.1 on 2025-01-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emergencia", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emergencia",
            name="estado",
            field=models.CharField(
                choices=[
                    ("1", "Amazonas"),
                    ("2", "Anzoátegui"),
                    ("3", "Apure"),
                    ("4", "Aragua"),
                    ("5", "Barinas"),
                    ("6", "Bolívar"),
                    ("7", "Carabobo"),
                    ("8", "Cojedes"),
                    ("9", "Delta Amacuro"),
                    ("10", "Falcón"),
                    ("11", "Guárico"),
                    ("12", "Lara"),
                    ("13", "Mérida"),
                    ("14", "Miranda"),
                    ("15", "Monagas"),
                    ("16", "Nueva Esparta"),
                    ("17", "Portuguesa"),
                    ("18", "Sucre"),
                    ("19", "Táchira"),
                    ("20", "Trujillo"),
                    ("21", "Vargas"),
                    ("22", "Yaracuy"),
                    ("23", "Zulia"),
                    ("24", "Distrito Capital"),
                ],
                max_length=2,
                verbose_name="Estado",
            ),
        ),
    ]
