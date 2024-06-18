from django.contrib.auth.models import Group, Permission


class UserAndPermissionFaker:
    group = None

    def create_group():
        self.group = Group.objects.create(name="administrador")

        print(f"Se ha creado el grupo {self.group}")

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
        self.group = Group.objects.create(name="administrador")

        print(f"Se ha creado el grupo {self.group}")

    def group_permissions():
        myGroup = self.group if self.group else Group.objects.get(name="administrador")
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
        myGroup = self.group if self.group else Group.objects.get(name="administrador")
        guest.groups.add(myGroup)
        print(f"Se ha asignado el grupo {myGroup} al usuario {guest}")
