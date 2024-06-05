from django.contrib import admin
from gestion_comunicacional.equipament.entities.EquipamentEntity import EquipamentEntity
from gestion_comunicacional.equipament.entities.EquipamentLoanEntity import (
    EquipamentLoanEntity,
)
from gestion_comunicacional.social_activity.entities.SocialActivityEntity import (
    SocialActivityEntity,
)
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import (
    SocialMediaAccountEntity,
)
from gestion_comunicacional.social_media.entities.SocialMediaPostEntity import (
    SocialMediaPostEntity,
)

admin.site.register(SocialMediaAccountEntity)
admin.site.register(SocialMediaPostEntity)
admin.site.register(SocialActivityEntity)
admin.site.register(EquipamentEntity)
admin.site.register(EquipamentLoanEntity)
