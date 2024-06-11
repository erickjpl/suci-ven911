from emergencia.entities.EmergencyEntity import EmergencyEntity

from django.forms import ModelForm, Select, Textarea, TextInput


class EmergencyForm(ModelForm):
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
        widgets = {
            "parroquia": Select(attrs={"class": "form-select mb-3"}),
            "organismo": Select(attrs={"class": "form-select mb-3"}),
            "incidencia": Select(attrs={"class": "form-select mb-3"}),
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
