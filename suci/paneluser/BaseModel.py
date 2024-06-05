from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_created",
    )
    datetime_created = models.DateTimeField(auto_now_add=True)
    user_updated = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated",
    )
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
