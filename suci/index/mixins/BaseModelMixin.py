from django.conf import settings
from django.contrib.auth import get_user
from django.db import models


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name="Creado por",
        on_delete=models.CASCADE,
        related_name="%(class)s_created",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name="Actualizado por",
        on_delete=models.CASCADE,
        related_name="%(class)s_updated",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Actualizado el",
    )
    deleted_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name="Eliminado por",
        on_delete=models.CASCADE,
        related_name="%(class)s_delete",
        null=True,
        blank=True,
    )
    deleted_at = models.DateTimeField(
        verbose_name="Eliminado el",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
