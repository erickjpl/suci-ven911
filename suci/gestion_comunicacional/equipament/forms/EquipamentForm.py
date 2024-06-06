from typing import Any, Mapping

from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm, TextInput
from django.forms.utils import ErrorList
from gestion_comunicacional.equipament.entities.EquipamentEntity import EquipamentEntity


class EquipamentForm(ModelForm):
    def __init__(self, *arg, **kwarg) -> None:
        super().__init__(*arg, **kwarg)
        for form in self.visible_fields():
            form.field.widget.attrs.update(
                {"class": "form-control mb-3", "autocomplete": "off"}
            )

    class Meta:
        model = EquipamentEntity
        fields = (
            "name",
            "description",
            "status",
        )
        exclude = [
            "id",
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        ]
        widgets = {
            "denunciante": TextInput(
                attrs={
                    "placeholder": "Ejem. George Harris",
                }
            ),
        }
