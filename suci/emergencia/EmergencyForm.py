from emergencia.entities.EmergencyEntity import EmergencyEntity

from django.forms import ModelForm, Select, Textarea, TextInput


class EmergencyForm(ModelForm):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        for form in self.visible_fields():
            form.field.widget.attrs.update({"class": "form-control", "autocomplete": "off"})

    class Meta:
        model = EmergencyEntity
        fields = [
            "parroquia",
            "organismo",
            "incidencia",
            "denunciante",
            "telefono_denunciante",
            "direccion_incidencia",
            "observaciones",
        ]
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "delete_at",
            "delete_by",
        ]
        widgets = {
            "parroquia": Select(attrs={"class": "mb-3"}),
            "organismo": Select(attrs={"class": "mb-3"}),
            "incidencia": Select(attrs={"class": "mb-3"}),
            "denunciante": TextInput(
                attrs={
                    "class": "mb-3",
                    "placeholder": "Ejem. George Harris",
                }
            ),
            "telefono_denunciante": TextInput(attrs={"class": "mb-3", "placeholder": "Ejem. 04125248935"}),
            "direccion_incidencia": Textarea(
                attrs={
                    "class": "mb-3",
                    "placeholder": "Ejem. Urbanización Lomas de Urdaneta",
                }
            ),
            "observaciones": Textarea(attrs={"class": "mb-3"}),
        }
