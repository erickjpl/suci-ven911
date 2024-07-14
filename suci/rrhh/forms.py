from django import forms
from .models import  Personal,Sexo, EstadoCivil,TallasCamisa, TallasPantalon, TallasZapatos, Grado, TipoPersonal, Cargo, Departamento, Sedes, Bienes, Sueldos, BonoGuerra, CestaTicket, SueldoMinimo, PrimaProfesionalismo


class FormPersonal(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            'estatus',
            'nombres',
            'apellidos',
            'nacionalidad',
            'cedula',
            'sexo',
            'fecha_nac',
            'edad',
            'telefono',
            'estado_civil',
            'conyugue',
            'cedula_conyugue',
            'tipo_sangre',
            'discapacitado',
            'talla_camisa',
            'talla_pantalon',
            'talla_zapato',
            'direccion',
            'nro_cuenta',
            'email',
            'grado_instruccion',
            'estudias',
            'comision_servicio',
            'pnb',
            'tipo_personal',
            'cargo',
            'fecha_ingreso_911',
            'fecha_ingreso_apn',
            'contratos',
            'departamento',
            'nino_menor_12',
            'edades1',
            'hijos_13_18',
            'nina_menor_12',
            'edades2',
            'hijos_discapacidad',
            'edades3',
            'motivo',
            'sede',
            'fasmij',
            'parentezco1',
            'beneficiario1',
            'cedula1',
            'direccion1',
            'parentezco2',
            'beneficiario2',
            'cedula2',
            'direccion2',
            'parentezco3',
            'beneficiario3',
            'cedula3',
            'direccion3',
            'fecha_retiro',
        ]
        widgets = {
            'estatus': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.Select(attrs={'class': 'form-control'}),
            'cedula': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateInput(attrs={'class': 'form-control', 'id': 'fecha_nac'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'conyugue': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula_conyugue': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control'}),
            'discapacitado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'talla_camisa': forms.Select(attrs={'class': 'form-control'}),
            'talla_pantalon': forms.Select(attrs={'class': 'form-control'}),
            'talla_zapato': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_cuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'grado_instruccion': forms.Select(attrs={'class': 'form-control'}),
            'estudia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comision_servicio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pnb': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tipo_personal': forms.Select(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_ingreso_911': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_ingreso_apn': forms.DateInput(attrs={'class': 'form-control'}),
            'contratos': forms.NumberInput(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'nino_menor_12': forms.NumberInput(attrs={'class': 'form-control'}),
            'edades1': forms.NumberInput(attrs={'class': 'form-control'}),
            'hijos_13_18': forms.NumberInput(attrs={'class': 'form-control'}),
            'edades2': forms.NumberInput(attrs={'class': 'form-control'}),
            'nina_menor_12': forms.NumberInput(attrs={'class': 'form-control'}),
            'edades3': forms.NumberInput(attrs={'class': 'form-control'}),
            'hijos_discapacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'edades4': forms.NumberInput(attrs={'class': 'form-control'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
            'sede': forms.Select(attrs={'class': 'form-control'}),
            'fasmij': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'parentezco1': forms.TextInput(attrs={'class': 'form-control'}),
            'beneficiario1': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula1': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion1': forms.TextInput(attrs={'class': 'form-control'}),
            'parentezco2': forms.TextInput(attrs={'class': 'form-control'}),
            'beneficiario2': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula2': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion2': forms.TextInput(attrs={'class': 'form-control'}),
            'parentezco3': forms.TextInput(attrs={'class': 'form-control'}),
            'beneficiario3': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula3': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion3': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_retiro': forms.DateInput(attrs={'class': 'form-control'}),
        }
        

class FormMovimientoPersonal(forms.ModelForm):

    class Meta:
        model = Personal
        fields = ['estatus', 'nombres', 'apellidos', 'nacionalidad', 'cedula', 'departamento','sede', 'motivo', 'fecha_retiro']
        

class FormEditarPersonal(forms.ModelForm):

    class Meta:
        model = Personal
        fields = ['estatus', 'nombres', 'apellidos', 'nacionalidad', 'cedula', 'sexo', 'fecha_nac', 'edad', 'telefono', 'estado_civil', 'conyugue', 'cedula_conyugue', 'tipo_sangre', 'discapacitado', 'talla_camisa', 'talla_pantalon', 'talla_zapato', 'direccion', 'nro_cuenta', 'email', 'grado_instruccion', 'estudias', 'comision_servicio', 'pnb', 'tipo_personal', 'cargo', 'fecha_ingreso_911', 'fecha_ingreso_apn', 'contratos', 'departamento', 'nino_menor_12', 'edades1', 'hijos_13_18', 'edades2', 'nina_menor_12', 'edades3', 'hijos_discapacidad', 'edades4', 'sede', 'motivo', 'fasmij', 'parentezco1', 'beneficiario1', 'cedula1', 'direccion1', 'parentezco2', 'beneficiario2', 'cedula2', 'direccion2', 'parentezco3', 'beneficiario3', 'cedula3', 'direccion3']
        
    
class FormEstadoC(forms.ModelForm):

    class Meta:
        model = EstadoCivil
        fields = ['estado_civil']


class GeneroFormSexo(forms.ModelForm):

    class Meta:
        model = Sexo
        fields = ['sexo']


class FormTallaC(forms.ModelForm):

    class Meta:
        model = TallasCamisa
        fields = ['estatus', 'talla_camisa', 'id' ]

class FormTallaP(forms.ModelForm):

    class Meta:
        model = TallasPantalon
        fields = ['estatus', 'talla_pantalon', 'id']

class FormTallaZ(forms.ModelForm):

    class Meta:
        model = TallasZapatos
        fields = ['estatus', 'talla_zapato', 'id' ]

class FormGradoI(forms.ModelForm):

    class Meta:
        model = Grado
        fields = ['grado_instruccion']

class FormTipoPersonal(forms.ModelForm):

    class Meta:
        model = TipoPersonal
        fields = ['tipo_personal']

class FormCargo(forms.ModelForm):

    class Meta:
        model = Cargo
        fields = ['estatus', 'cargo', 'id']

class FormDepartamento(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = ['estatus', 'departamento', 'id' ]

class FormSedes(forms.ModelForm):

    class Meta:
        model = Sedes
        fields = ['estatus', 'sede', 'id']


class FormBienes(forms.ModelForm):

    class Meta:
        model = Bienes
        fields = ['id','estatus', 'sede', 'departamento', 'nombre', 'cantidad']
        
        
class FormSueldos(forms.ModelForm):

    class Meta:
        model = Sueldos
        fields = ['estatus', 'sueldo_base', 'prima_profesionalismo', 'p_discapacidad', 'p_hijos_menor_12', 'p_hijas_menor_12', 'p_hijos_12_18', 'p_hijos_discapacidad', 'n_fasmij', 'cesta_t', 'monto_t', 'b_guerra', 'monto_b', 'personal']
    

class FormBonoGuerra(forms.ModelForm):

    class Meta:
        model = BonoGuerra
        fields = ['estatus', 'monto' , 'id']
        
        
class FormCestaTicket(forms.ModelForm):

    class Meta:
        model = CestaTicket
        fields = ['estatus', 'monto' , 'id']
class FormSueldoMinimo(forms.ModelForm):

    class Meta:
        model = SueldoMinimo
        fields = ['estatus', 'monto' , 'id']
class FormPrima(forms.ModelForm):

    class Meta:
        model = PrimaProfesionalismo
        fields = ['id', 'estatus' , 'porcentaje']
        
class FormPrimaAdd(forms.ModelForm):

    class Meta:
        model = PrimaProfesionalismo
        fields = ['id', 'estatus' , 'titulo', 'porcentaje']