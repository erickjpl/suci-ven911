from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from paneluser.models import UserEntity

admin.site.register(UserEntity, UserAdmin)
admin.site.register(Permission)
