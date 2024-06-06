from django.forms import ModelForm, TextInput
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
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "delete_at",
            "delete_by",
        ]
        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Ingrese el equipo (Marca, Modelo)",
                }
            ),
            "description": TextInput(
                attrs={
                    "placeholder": "Ingrese la descripcion",
                }
            ),
        }
