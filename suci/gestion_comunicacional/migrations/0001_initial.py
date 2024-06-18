# Generated by Django 5.0.6 on 2024-06-18 15:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EquipmentEntity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "deleted",
                    models.BooleanField(default=False, verbose_name="Está eliminado"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Eliminado el"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Equipo")),
                (
                    "description",
                    models.TextField(verbose_name="Descripción del equipo"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("available", "Disponible"),
                            ("loaned", "Prestado"),
                            ("maintenance", "Mantenimiento"),
                        ],
                        max_length=50,
                        verbose_name="Estatus del equipo",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_created",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creado por",
                    ),
                ),
                (
                    "deleted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_delete",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Eliminado por",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_updated",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Actualizado por",
                    ),
                ),
            ],
            options={
                "verbose_name": "Equipo",
                "verbose_name_plural": "Equipos",
                "db_table": "gc_equipments",
                "ordering": ["status"],
            },
        ),
        migrations.CreateModel(
            name="EquipmentLoanEntity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "department",
                    models.CharField(max_length=100, verbose_name="Departamento"),
                ),
                ("loan_date", models.DateField(verbose_name="Fecha del préstamo")),
                (
                    "return_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de devolución"
                    ),
                ),
                (
                    "equipments",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gc.equipmententity",
                        verbose_name="Equipo ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Equipo prestado",
                "verbose_name_plural": "Equipos prestados",
                "db_table": "gc_equipments_loans",
                "ordering": ["equipments"],
            },
        ),
        migrations.CreateModel(
            name="SocialActivityEntity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "deleted",
                    models.BooleanField(default=False, verbose_name="Está eliminado"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Eliminado el"
                    ),
                ),
                (
                    "activity_type",
                    models.CharField(
                        choices=[
                            ("workshop", "Taller"),
                            ("conference", "Conferencia"),
                            ("campaign", "Campaña"),
                        ],
                        max_length=50,
                        verbose_name="Tipo de actividad",
                    ),
                ),
                ("date", models.DateField(verbose_name="Fecha de la actividad")),
                (
                    "location",
                    models.CharField(
                        max_length=255, verbose_name="Lugar de la actividad"
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Descripcion de la actividad"),
                ),
                (
                    "reason",
                    models.TextField(verbose_name="Motivo para realizar la actividad"),
                ),
                (
                    "beneficiaries",
                    models.IntegerField(
                        verbose_name="Cantidad de personas beneficiadas"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_created",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creado por",
                    ),
                ),
                (
                    "deleted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_delete",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Eliminado por",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_updated",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Actualizado por",
                    ),
                ),
            ],
            options={
                "verbose_name": "Actividad social",
                "verbose_name_plural": "Actividades sociales",
                "db_table": "gc_social_activities",
                "ordering": ["activity_type"],
                "permissions": [
                    ("view_social_activity", "Can view social activity"),
                    ("add_social_activity", "Can add social activity"),
                    ("change_social_activity", "Can change social activity"),
                    ("delete_social_activity", "Can delete social activity"),
                ],
            },
        ),
        migrations.CreateModel(
            name="SocialMediaAccountEntity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "deleted",
                    models.BooleanField(default=False, verbose_name="Está eliminado"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Eliminado el"
                    ),
                ),
                (
                    "platform",
                    models.CharField(
                        choices=[
                            ("Facebook", "Facebook"),
                            ("Instagram", "Instagram"),
                            ("Twitter", "Twitter"),
                        ],
                        max_length=50,
                        verbose_name="Red social",
                    ),
                ),
                (
                    "username_sm",
                    models.CharField(
                        max_length=60,
                        unique=True,
                        verbose_name="Nombre de usuario de la red social",
                    ),
                ),
                ("url", models.URLField(unique=True, verbose_name="Direccion web")),
                (
                    "followers",
                    models.PositiveSmallIntegerField(verbose_name="Seguidores"),
                ),
                (
                    "responsible",
                    models.CharField(
                        max_length=100, verbose_name="Responsable de la red social"
                    ),
                ),
                (
                    "publications",
                    models.PositiveSmallIntegerField(verbose_name="Publicaciones"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_created",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creado por",
                    ),
                ),
                (
                    "deleted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_delete",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Eliminado por",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_updated",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Actualizado por",
                    ),
                ),
            ],
            options={
                "verbose_name": "Red social",
                "verbose_name_plural": "Redes sociales",
                "db_table": "gc_social_media_accounts",
                "ordering": ["platform"],
            },
        ),
        migrations.CreateModel(
            name="SocialMediaPostEntity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "post_type",
                    models.CharField(
                        choices=[
                            ("reel", "Reel"),
                            ("post", "Post"),
                            ("story", "Story"),
                            ("picture", "Picture"),
                        ],
                        max_length=50,
                        verbose_name="Tipo de publicacion",
                    ),
                ),
                ("content", models.TextField(verbose_name="Contenido")),
                ("publish_date", models.DateField(verbose_name="Fecha de publicacion")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("published", "Published"),
                            ("scheduled", "Scheduled"),
                            ("draft", "Draft"),
                        ],
                        max_length=50,
                        verbose_name="Estatus",
                    ),
                ),
                (
                    "reach",
                    models.IntegerField(verbose_name="Alcance de la publicación"),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gc.socialmediaaccountentity",
                        verbose_name="Cuenta",
                    ),
                ),
            ],
            options={
                "verbose_name": "Publicacion de red social",
                "verbose_name_plural": "Publicaciones de redes sociales",
                "db_table": "gc_social_media_posts",
                "ordering": ["account"],
            },
        ),
    ]
