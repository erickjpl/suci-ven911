from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class UserAndPermissionFaker:
    group = None

    def create_permissions():
        socialActivity = ContentType.objects.get_for_model(SocialActivityEntity)
        permissions = [
            # """ Social Activity """
            ("view_social_activity", "Can view social activity", socialActivity),
            ("add_social_activity", "Can add social activity", socialActivity),
            ("change_social_activity", "Can change social activity", socialActivity),
            ("delete_social_activity", "Can delete social activity", socialActivity),
        ]
        for codename, name, content_type in permissions:
            Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)
        print(f"Se han registrado {str(len(permissions))} permisos")

    def user_permissions(guest):
        permissions = Permission.objects.filter(
            codename__in=[
                "view_social_activity",
                "add_social_activity",
                "change_social_activity",
            ]
        )
        for permission in permissions:
            guest.user_permissions.add(permission)
        print(f"Se han asignado {str(permissions.count())} permisos al usuario {guest}")

    def create_group():
        UserAndPermissionFaker.group = Group.objects.create(name="administrador")
        print(f"Se ha creado el grupo {UserAndPermissionFaker.group}")

    def group_permissions():
        myGroup = (
            UserAndPermissionFaker.group if UserAndPermissionFaker.group else Group.objects.get(name="administrador")
        )
        permissions = Permission.objects.filter(
            codename__in=[
                "view_social_activity",
                "add_social_activity",
                "change_social_activity",
                "delete_social_activity",
            ]
        )
        for permission in permissions:
            myGroup.permissions.add(permission)
        print(f"Se han asignado {str(permissions.count())} permisos al grupo {myGroup}")

    def user_groups(guest):
        myGroup = (
            UserAndPermissionFaker.group if UserAndPermissionFaker.group else Group.objects.get(name="administrador")
        )
        guest.groups.add(myGroup)
        print(f"Se ha asignado el grupo {myGroup} al usuario {guest}")
