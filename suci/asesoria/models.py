from django.db import models

# Create your models here.
class RegistroFilmico(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    camara = models.CharField(max_length=50, blank=True, null=True)
    motivo_solicitud = models.CharField(max_length=400)
    ente_solicita = models.CharField(max_length=50, blank=True, null=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    fecha_culminacion = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "registro_filmico"
        verbose_name_plural = "registro_filmicos"
        
    def __str__(self):
        return self.camara
    
    
class Denuncia(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    ente = models.CharField(max_length=50, blank=True, null=True)
    nombres_d = models.CharField(max_length=50)
    apellidos_d = models.CharField(max_length=50)
    cedula_d = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)
    email = models.EmailField(blank=True, null=True)
    direccion_d = models.CharField(max_length=150)
    nombres_denunciado = models.CharField(max_length=50, blank=True, null=True)
    apellidos_denunciado = models.CharField(max_length=50, blank=True, null=True)
    cedula_denunciado = models.CharField(max_length=50, blank=True, null=True)
    motivo = models.CharField(max_length=400)
    zona = models.CharField(max_length=150, blank=True, null=True)
    fecha_denuncia = models.DateField()
    fecha_incidente = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "denuncia"
        verbose_name_plural = "denuncias"
        
    def __str__(self):
        return self.ente
    
    

