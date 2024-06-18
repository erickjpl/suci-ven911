from django.db import models


class Departamentos(models.Model):
    departamento = models.CharField(max_length=64, verbose_name="Departamento:", default="", unique=True)
    estado = models.CharField(max_length=64, verbose_name="Estado:", default="", unique=True)


class Sedes(models.Model):
    direccion = models.CharField(max_length=64, verbose_name="Direccion:", default="", unique=True)
    municipio = models.CharField(max_length=64, verbose_name="Municipio:", default="", unique=True)
    estado = models.CharField(max_length=64, verbose_name="Estado:", default="", unique=True)


from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserEntity(AbstractUser):
    image = models.ImageField(
        upload_to="users/%Y/%m/%d",
        verbose_name="Foto del perfil",
        name="photo",
        null=True,
        blank=True,
    )
    dni = models.CharField(
        verbose_name="Cédula de identidad",
        name="dni",
        max_length=10,
        unique=True,
        error_messages={
            "unique": "Un usuario con ese número de cédula ya existe",
        },
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "dni"
    REQUIRED_FIELDS = ["username", "email"]

    def get_image(self):
        if self.image:
            return "{}{}".format(settings.MEDIA_URL, self.image)
        else:
            return "{}{}".format(settings.STATIC_URL, "img/admin.png")

    def __str__(self):
        return f"{self.username} - {self.dni}"
