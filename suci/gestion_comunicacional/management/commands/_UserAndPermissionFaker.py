from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class UserAndPermissionFaker:
    group = None

    def create_permissions():
        socialActivity = ContentType.objects.get_for_model(SocialActivityEntity)
        socialMedia = ContentType.objects.get_for_model(SocialMediaAccountEntity)
        permissions = [
            # """ Social Activity """
            (SocialActivityEntity.PERMISSION_VIEW_SOCIAL_ACTIVITY, "Can view social activity", socialActivity),
            (SocialActivityEntity.PERMISSION_ADD_SOCIAL_ACTIVITY, "Can add social activity", socialActivity),
            (SocialActivityEntity.PERMISSION_CHANGE_SOCIAL_ACTIVITY, "Can change social activity", socialActivity),
            (SocialActivityEntity.PERMISSION_DELETE_SOCIAL_ACTIVITY, "Can delete social activity", socialActivity),
            # """ Social Media """
            (SocialMediaAccountEntity.PERMISSION_VIEW_SOCIAL_MEDIA, "Can view social media", socialMedia),
            (SocialMediaAccountEntity.PERMISSION_ADD_SOCIAL_MEDIA, "Can add social media", socialMedia),
            (SocialMediaAccountEntity.PERMISSION_CHANGE_SOCIAL_MEDIA, "Can change social media", socialMedia),
            (SocialMediaAccountEntity.PERMISSION_DELETE_SOCIAL_MEDIA, "Can delete social media", socialMedia),
        ]
        for codename, name, content_type in permissions:
            Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)
        print(f"Se han registrado {str(len(permissions))} permisos")

    def user_permissions(guest):
        permissions = Permission.objects.filter(
            codename__in=[
                # Social Activity
                SocialActivityEntity.PERMISSION_VIEW_SOCIAL_ACTIVITY,
                SocialActivityEntity.PERMISSION_ADD_SOCIAL_ACTIVITY,
                SocialActivityEntity.PERMISSION_CHANGE_SOCIAL_ACTIVITY,
                # Social Media
                SocialMediaAccountEntity.PERMISSION_VIEW_SOCIAL_MEDIA,
                SocialMediaAccountEntity.PERMISSION_ADD_SOCIAL_MEDIA,
                SocialMediaAccountEntity.PERMISSION_CHANGE_SOCIAL_MEDIA,
            ]
        )
        for permission in permissions:
            guest.user_permissions.add(permission)
        print(f"Se han asignado {str(permissions.count())} permisos al usuario {guest.username}")
