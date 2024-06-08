from django.forms import ModelForm

from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity


class SocialActivityForm(ModelForm):
    class Meta:
        model = SocialActivityEntity
        fields = (
            "date",
            "location",
            "activity_type",
            "reason",
            "description",
            "beneficiaries",
        )
