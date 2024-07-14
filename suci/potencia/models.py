from django.db import models

class Incidencias(models.Model):
    estado=models.CharField(max_length=300)
    sede=models.CharField(max_length=300)
    departamento=models.CharField(max_length=300)
    tipoincidencia=models.CharField(max_length=300)
    usuario=models.CharField(max_length=300)
    observaciones=models.CharField(max_length=300)
    tiposolicitud=models.CharField(max_length=350)

    class Meta:
        verbose_name='incidencia'
        verbose_name_plural='incidencias'

    def __str__(self):
        return self.estado
