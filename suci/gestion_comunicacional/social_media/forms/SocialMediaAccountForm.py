from django.forms import ModelForm, TextInput
from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import (
    SocialMediaAccountEntity,
)


class SocialMediaAccountForm(ModelForm):
    def __init__(self, *arg, **kwarg) -> None:
        super().__init__(*arg, **kwarg)
        for form in self.visible_fields():
            form.field.widget.attrs.update(
                {"class": "form-control mb-3", "autocomplete": "off"}
            )

    class Meta:
        model = SocialMediaAccountEntity
        fields = (
            "platform",
            "username",
            "url",
            "followers",
            "responsible",
            "publications",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "delete_at",
            "delete_by",
        ]
        widgets = {
            "platform": TextInput(
                attrs={
                    "placeholder": "Ingrese el nombre de la red social",
                }
            ),
            "username": TextInput(
                attrs={
                    "placeholder": "Ingrese el usuario de la red social",
                }
            ),
            "url": TextInput(
                attrs={
                    "placeholder": "Ingrese la url de la red social",
                }
            ),
            "followers": TextInput(
                attrs={
                    "placeholder": "Ingrese la cantidad de seguidores de la red social",
                }
            ),
            "responsible": TextInput(
                attrs={
                    "placeholder": "Ingrese el usuario responsable de la red social",
                }
            ),
            "publications": TextInput(
                attrs={
                    "placeholder": "Ingrese la cantidad de publicaciones de la red social",
                }
            ),
        }
