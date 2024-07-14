from gestion_comunicacional.mixins.BaseModelMixin import BaseModel

from django.db.models import CharField, PositiveSmallIntegerField, URLField
from django.forms import model_to_dict


class SocialMediaAccountEntity(BaseModel):
    PERMISSION_VIEW_SOCIAL_MEDIA = "view_social_media"
    PERMISSION_ADD_SOCIAL_MEDIA = "add_social_media"
    PERMISSION_CHANGE_SOCIAL_MEDIA = "change_social_media"
    PERMISSION_DELETE_SOCIAL_MEDIA = "delete_social_media"
    
    VIEW_SOCIAL_MEDIA = "gc:view_social_media"
    ADD_SOCIAL_MEDIA = "gc:add_social_media"
    CHANGE_SOCIAL_MEDIA = "gc:change_social_media"
    DELETE_SOCIAL_MEDIA = "gc:delete_social_media"
    
    PLATFORM_CHOICES = [
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("Twitter", "Twitter"),
    ]

    platform = CharField(max_length=50, verbose_name="Red social", choices=PLATFORM_CHOICES)
    username_sm = CharField(max_length=60, verbose_name="Nombre de usuario de la red social", unique=True)
    url = URLField(verbose_name="Direccion web", unique=True)
    followers = PositiveSmallIntegerField("Seguidores")
    responsible = CharField(max_length=100, verbose_name="Responsable de la red social")
    publications = PositiveSmallIntegerField("Publicaciones")

    def __str__(self):
        return f"red social: {self.platform}@{self.username_sm}"

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        db_table = "gc_social_media_accounts"
        verbose_name = "Red social"
        verbose_name_plural = "Redes sociales"
        ordering = ["platform"]
