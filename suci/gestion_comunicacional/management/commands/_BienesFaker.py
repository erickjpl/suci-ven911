import random

from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from rrhh.models import Bienes, Departamento, Sedes

from django.db.models import Q


class BienesFaker:
    departamento = None
    sede = None
    
    def add_departamento():
        BienesFaker.departamento = Departamento.objects.filter(departamento='Gestion Comunicacional').first()
        if BienesFaker.departamento is None:
            BienesFaker.departamento = Departamento.objects.create(
                departamento='Gestion Comunicacional',
                estatus='ACTIVO',
            )
        count = Departamento.objects.count()
        print(f"Hay {count} departamentos en la base de datos")

    def add_sedes():
        BienesFaker.sede = Sedes.objects.filter(sede='Gestion Comunicacional').first()
        if BienesFaker.sede is None:
          BienesFaker.sede = Sedes.objects.create(
              sede='Caracas',
              estatus='ACTIVO',
          )
        count = Sedes.objects.count()
        print(f"Hay {count} sedes en la base de datos")
        
    def add_bienes(fake):
        for _ in range(15):
            Bienes.objects.create(
                estatus='ACTIVO',
                sede=BienesFaker.sede,
                departamento=BienesFaker.departamento,
                nombre=fake.bien_nacional(),
                cantidad=random.randint(1, 18),
            )
        count = Bienes.objects.count()
        print(f"Hay {count} bienes en la base de datos")
