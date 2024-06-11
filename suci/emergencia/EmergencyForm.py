from emergencia.entities.EmergencyEntity import EmergencyEntity

from django.forms import ModelForm, Select, Textarea, TextInput


class EmergencyForm(ModelForm):
    class Meta:
        model = EmergencyEntity
        fields = [
            "parroquia_id",
            "organismo_id",
            "incidencia_id",
            "denunciante",
            "telefono_denunciante",
            "direccion_incidencia",
            "observaciones",
        ]
        widgets = {
            "parroquia_id": Select(attrs={"class": "form-select mb-3"}),
            "organismo_id": Select(attrs={"class": "form-select mb-3"}),
            "incidencia_id": Select(attrs={"class": "form-select mb-3"}),
            "denunciante": TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ejem. George Harris",
                }
            ),
            "telefono_denunciante": TextInput(attrs={"class": "form-control mb-3", "placeholder": "Ejem. 04125248935"}),
            "direccion_incidencia": Textarea(
                attrs={
                    "class": "form-control mb-3",
                    "placeholder": "Ejem. Urbanización Lomas de Urdaneta",
                }
            ),
            "observaciones": Textarea(attrs={"class": "form-control mb-3"}),
        }
