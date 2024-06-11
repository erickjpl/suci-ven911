from index.mixins.BaseModelMixin import BaseModel

from django.db.models import CASCADE, CharField, ForeignKey, Model


class CuadrantePazEntity(Model):
    nombre = CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "eme_cuadrantes_paz"
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["nombre"]


class EstadoEntity(Model):
    nombre = CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "general_estados"
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["nombre"]


class CiudadEntity(Model):
    nombre = CharField(max_length=100)
    estado = ForeignKey(EstadoEntity, on_delete=CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "general_ciudades"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["nombre"]


class MunicipioEntity(Model):
    nombre = CharField(max_length=100)
    estado = ForeignKey(EstadoEntity, on_delete=CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "general_municipios"
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["nombre"]


class ParroquiaEntity(Model):
    nombre = CharField(max_length=100)
    # id_estado = ForeignKey(Estado, on_delete=CASCADE)
    municipio = ForeignKey(MunicipioEntity, on_delete=CASCADE)
    cuadrante_paz = ForeignKey(CuadrantePazEntity, on_delete=CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "general_parroquias"
        verbose_name = "Parroquia"
        verbose_name_plural = "Parroquias"
        ordering = ["nombre"]
