from django.db import models


class ProfileEntity(models.Model):

    STATUS = (
        ("estandar", "estandar"),
        ("admin", "admin"),
        ("superu", "superu"),
    )

    username = models.CharField(
        max_length=200, verbose_name="Cédula:", default="", unique=True
    )
    nombre = models.CharField(max_length=200, verbose_name="Nombre:", default="")
    apellido = models.CharField(max_length=200, verbose_name="Apellido:", default="")
    password = models.CharField(max_length=200, verbose_name="Contraseña:", default="")
    tipo = models.CharField(
        max_length=200, verbose_name="Tipo de Usuario:", choices=STATUS, default=""
    )
    sede = models.CharField(max_length=200, verbose_name="Sede:", default="")
    departamento = models.CharField(
        max_length=200, verbose_name="Departamento:", default=""
    )
    estado = models.CharField(max_length=200, verbose_name="Estado:", default="")
    correo = models.EmailField(max_length=200, verbose_name="Correo:", default="")

    def __str__(self):
        return self.username
