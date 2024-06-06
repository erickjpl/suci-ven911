from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_created",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated",
    )
    updated_at = models.DateTimeField(auto_now=True)
    delete_by = models.ForeignKey(
        null=True,
        blank=True,
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_delete",
    )
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
