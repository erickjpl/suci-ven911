from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
#from .models import Nacionalidad, Sexo, EstadoCivil, Sangre, TallasCamisa, TallasPantalon, TallasZapatos, Grado, TipoPersonal, Cargo, Departamento, Sedes

# Create your models here.

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "nacionalidad"
        verbose_name_plural = "nacionalidades"
        
    def __str__(self):
        return self.nacionalidad
    
    
class Sexo(models.Model):
    sexo = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "sexo"
        verbose_name_plural = "sexos"
        
    def __str__(self):
        return self.sexo
    
    
class EstadoCivil(models.Model):
    estado_civil = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "estado_civil"
        verbose_name_plural = "estados_civiles"
        
    def __str__(self):
        return self.estado_civil
    
    
class Sangre(models.Model):
    tipo_sangre = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "tipo_sangre"
        verbose_name_plural = "tipos_sangre"
        
    def __str__(self):
        return self.tipo_sangre
    

class TallasCamisa(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    talla_camisa = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "talla_camisa"
        verbose_name_plural = "tallas_camisas"
        
    def __str__(self):
        return self.talla_camisa
    
    
class TallasPantalon(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    talla_pantalon = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "talla_pantalon"
        verbose_name_plural = "tallas_pantalones"
        
    def __str__(self):
        return self.talla_pantalon
    
    
class TallasZapatos(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    talla_zapato = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "talla_zapato"
        verbose_name_plural = "tallas_zapatos"
        
    def __str__(self):
        return self.talla_zapato
    

class Grado(models.Model):
    grado_instruccion = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "grado_instruccion"
        verbose_name_plural = "grados_instruccion"
        
    def __str__(self):
        return self.grado_instruccion
    
    
class TipoPersonal(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    tipo_personal = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "tipo_personal"
        verbose_name_plural = "tipos_personales"
        
    def __str__(self):
        return self.tipo_personal
    

class Cargo(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "cargo"
        verbose_name_plural = "cargos"
        
    def __str__(self):
        return self.cargo
    

class Departamento(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"
        
    def __str__(self):
        return self.departamento
    
    
class Sedes(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    sede = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "sede"
        verbose_name_plural = "sedes"
        
    def __str__(self):
        return self.sede


class Personal(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    cedula = models.IntegerField()
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    fecha_nac = models.DateField()
    edad = models.IntegerField()
    telefono = models.CharField(max_length=11)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    conyugue = models.CharField(max_length=50, blank=True, null=True)
    cedula_conyugue = models.IntegerField(blank=True, null=True)
    tipo_sangre = models.ForeignKey(Sangre, on_delete=models.CASCADE)    
    discapacitado = models.BooleanField()
    talla_camisa = models.ForeignKey(TallasCamisa, on_delete=models.CASCADE) 
    talla_pantalon = models.ForeignKey(TallasPantalon, on_delete=models.CASCADE) 
    talla_zapato = models.ForeignKey(TallasZapatos, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=150)
    nro_cuenta = models.CharField(max_length=25)
    email = models.EmailField(blank=True, null=True)
    grado_instruccion = models.ForeignKey(Grado, on_delete=models.CASCADE) 
    estudias = models.BooleanField()
    comision_servicio = models.BooleanField()
    pnb = models.BooleanField()
    tipo_personal = models.ForeignKey(TipoPersonal, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    fecha_ingreso_911 = models.DateField()
    fecha_ingreso_apn = models.DateField()
    contratos = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nino_menor_12 = models.CharField(max_length=2,blank=True, null=True)
    edades1 = models.IntegerField(blank=True, null=True)
    hijos_13_18 = models.CharField(max_length=2, blank=True, null=True)
    edades2 = models.IntegerField(blank=True, null=True)
    nina_menor_12 = models.CharField(max_length=2,blank=True, null=True)
    edades3 = models.IntegerField(blank=True, null=True)
    hijos_discapacidad = models.CharField(max_length=2,blank=True, null=True)
    edades4 = models.IntegerField(blank=True, null=True)
    motivo = models.CharField(max_length=50, blank=True, null=True)
    fecha_retiro = models.DateField(blank=True, null=True, default = '')
    sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)
    fasmij = models.BooleanField()
    parentezco1 = models.CharField(max_length=10, blank=True, null=True)
    beneficiario1 = models.CharField(max_length=50, blank=True, null=True)
    cedula1 = models.CharField(max_length=50, blank=True, null=True)
    direccion1 = models.CharField(max_length=150, blank=True, null=True)
    parentezco2 = models.CharField(max_length=10, blank=True, null=True)
    beneficiario2 = models.CharField(max_length=50, blank=True, null=True)
    cedula2 = models.CharField(max_length=50, blank=True, null=True)
    direccion2 = models.CharField(max_length=150, blank=True, null=True)
    parentezco3 = models.CharField(max_length=10, blank=True, null=True)
    beneficiario3 = models.CharField(max_length=50, blank=True, null=True)
    cedula3 = models.CharField(max_length=50, blank=True, null=True)
    direccion3 = models.CharField(max_length=150, blank=True, null=True)
    #creador = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "personal"
        verbose_name_plural = "personales"
        
    def __str__(self):
        return self.nombres
    

class Bienes(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20,blank=True, null=True)
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "bien"
        verbose_name_plural = "bienes"
        
    def __str__(self):
        return self.nombre
    
    
    
class CestaTicket(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "cestaticket"
        verbose_name_plural = "cestatickets"
        
    def __str__(self):
        return self.descripcion
    
class BonoGuerra(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "bonoguerra"
        verbose_name_plural = "bonosguerras"
        
    def __str__(self):
        return self.descripcion
    
    
class Tasa(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "tasabcv"
        verbose_name_plural = "tasasbcv"
        
    def __str__(self):
        return self.descripcion
    

class PrimaProfesionalismo(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    titulo = models.ForeignKey(Grado, on_delete=models.CASCADE) 
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "prima_profesional"
        verbose_name_plural = "primas_prosesionales"
        
    def __str__(self):
        return self.titulo.grado_instruccion
    
class SueldoMinimo(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "sueldominimo"
        verbose_name_plural = "sueldosminimo"
        
    def __str__(self):
        return self.descripcion
    
class Sueldos(models.Model):
    estatus = models.CharField(max_length=50, blank=True, null=True)
    sueldo_base = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prima_profesionalismo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_discapacidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_hijos_menor_12 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_hijas_menor_12 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_hijos_12_18 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_hijos_discapacidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    n_fasmij = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cesta_t = models.BooleanField()
    monto_t = models.ForeignKey(CestaTicket, on_delete=models.CASCADE)
    b_guerra = models.BooleanField()
    monto_b = models.ForeignKey(BonoGuerra, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "sueldo"
        verbose_name_plural = "sueldos"
        
    def __str__(self):
        return self.estatus
    

