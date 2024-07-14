
//  JAVASCRIPT PARA ADD PERSONAL

$(document).ready(function() {
    $('#myBtnAdd').click(function() {
        $('#addpersonal').modal('show');
    });
});


//  JAVASCRIPT PARA UPDATE PERSONAL

$('.btn-editar').click(function() {

    let id_persona = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-edicion/' + id_persona,
        method: 'GET',
        success: function(response) {
            
            let id = response.id;
            let estatus = response.estatus;
            let nombre = response.nombres;
            let apellido = response.apellidos;
            let cedula = response.cedula;
            let nacionalidad = response.nacionalidad;
            let sexo = response.sexo;
            let fecha_nac = response.fecha_nac;
            let edad = response.edad;
            let telefono = response.telefono;
            let estado_civil = response.estado_civil;
            let conyugue = response.conyugue;
            let ciconyugue = response.ciconyugue;
            if (ciconyugue == "None") {
                ciconyugue = "";
            }
            let tipo_sangre = response.tipo_sangre;
            let discapacitado = response.discapacitado;
            let talla_camisa = response.talla_camisa;
            let talla_pantalon = response.talla_pantalon;
            let talla_zapato = response.talla_zapato;
            let direccion = response.direccion;
            let nro_cuenta= response.nro_cuenta;
            let email = response.email;
            let grado_instruccion = response.grado_instruccion;
            let estudias = response.estudias;
            let comision_servicio = response.comision_servicio;
            let pnb = response.pnb;
            let tipo_personal = response.tipo_personal;
            let cargo = response.cargo;
            let fecha_ingreso_911 = response.fecha_ingreso_911;
            let fecha_ingreso_apn = response.fecha_ingreso_apn;
            let contratos = response.contratos;
            let nino_menor_12 = response.nino_menor_12;
            let edades1 = response.edades1;
            let hijos_13_18 = response.hijos_13_18;
            let edades2 = response.edades2;
            let nina_menor_12 = response.nina_menor_12;
            let edades3 = response.edades3;
            let hijos_discapacidad = response.hijos_discapacidad;
            let edades4 = response.edades4;
            let fasmij = response.fasmij;
            let parentezco1 = response.parentezco1;
            let parentezco2 = response.parentezco2;
            let parentezco3 = response.parentezco3;
            let beneficiario1 = response.beneficiario1;
            let beneficiario2 = response.beneficiario2;
            let beneficiario3 = response.beneficiario3;
            let cedula1 = response.cedula1;
            let cedula2 = response.cedula2;
            let cedula3 = response.cedula3;
            let direccion1 = response.direccion1;
            let direccion2 = response.direccion2;
            let direccion3 = response.direccion3;
            let departamento = response.departamento;
            let sede = response.sede;
            let motivo = response.motivo;
            if (motivo == "None") {
                motivo = "";
            }
            document.getElementById("id_persona_e").value = estatus;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("nacionalidad_e").value = nacionalidad;
            document.getElementById("cedula_e").value = cedula;
            document.getElementById("nombres_e").value = nombre;
            document.getElementById("apellidos_e").value = apellido;
            document.getElementById("sexo_e").value = sexo;
            document.getElementById("edad_e").value = edad;
            document.getElementById("fecha_nac_e").value = fecha_nac;
            document.getElementById("telefono_e").value = telefono;
            document.getElementById("estado_civil_e").value = estado_civil;
            document.getElementById("conyugue_e").value = conyugue;
            document.getElementById("cedula_conyugue_e").value = ciconyugue;
            document.getElementById("tipo_sangre_e").value = tipo_sangre;
            document.getElementById("discapacitado_e").value = discapacitado;
            document.getElementById("talla_camisa_e").value = talla_camisa;
            document.getElementById("talla_pantalon_e").value = talla_pantalon;
            document.getElementById("talla_zapato_e").value = talla_zapato;
            document.getElementById("direccion_e").value = direccion;
            document.getElementById("nro_cuenta_e").value = nro_cuenta;
            document.getElementById("email_e").value = email;
            document.getElementById("grado_instruccion_e").value = grado_instruccion;
            document.getElementById("estudias_e").value = estudias;
            document.getElementById("comision_servicio_e").value = comision_servicio;
            document.getElementById("pnb_e").value = pnb;
            document.getElementById("tipo_personal_e").value = tipo_personal;
            document.getElementById("cargo_e").value = cargo;
            document.getElementById("fecha_ingreso_911_e").value = fecha_ingreso_911;
            document.getElementById("fecha_ingreso_apn_e").value = fecha_ingreso_apn;
            document.getElementById("contratos_e").value = contratos;
            document.getElementById("nino_menor_12_e").value = nino_menor_12;
            document.getElementById("edades1_e").value = edades1;
            document.getElementById("hijos_13_18_e").value = hijos_13_18;
            document.getElementById("edades2_e").value = edades2;
            document.getElementById("nina_menor_12_e").value = nina_menor_12;
            document.getElementById("edades3_e").value = edades3;
            document.getElementById("hijos_discapacidad_e").value = hijos_discapacidad;
            document.getElementById("edades4_e").value = edades4;
            document.getElementById("fasmij_e").value = fasmij;
            document.getElementById("parentezco1_e").value = parentezco1;
            document.getElementById("parentezco2_e").value = parentezco2;
            document.getElementById("parentezco3_e").value = parentezco3;
            document.getElementById("beneficiario1_e").value = beneficiario1;
            document.getElementById("beneficiario2_e").value = beneficiario2;
            document.getElementById("beneficiario3_e").value = beneficiario3;
            document.getElementById("cedula1_e").value = cedula1;
            document.getElementById("cedula2_e").value = cedula2;
            document.getElementById("cedula3_e").value = cedula3;
            document.getElementById("direccion1_e").value = direccion1;
            document.getElementById("direccion2_e").value = direccion2;
            document.getElementById("direccion3_e").value = direccion3;
            document.getElementById("departamento_e").value = departamento;
            document.getElementById("sede_e").value = sede;
            document.getElementById("motivo_e").value = motivo;
        
            $('#updpersonal').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});


//  JAVASCRIPT PARA UPDATE MOVIMIENTO PERSONAL

$('.btn-editar-mov').click(function() {

    let id_persona = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos/' + id_persona,
        method: 'GET',
        success: function(response) {
            
            let id = response.id;
            let estatus = response.estatus;
            let nombre = response.nombres;
            let apellido = response.apellidos;
            let cedula = response.cedula;
            let nacionalidad = response.nacionalidad;
            let departamento = response.departamento;
            let sede = response.sede;
            let motivo = response.motivo;
            if (motivo == "None") {
                motivo = "";
            }
            let fecha_retiro = response.fecha_retiro;
            document.getElementById("id_persona_m").value = estatus
            document.getElementById("estatus_m").value = estatus
            document.getElementById("nacionalidad_m").value = nacionalidad
            document.getElementById("cedula_m").value = cedula
            document.getElementById("nombres_m").value = nombre
            document.getElementById("apellidos_m").value = apellido
            document.getElementById("departamento_m").value = departamento
            document.getElementById("sede_m").value = sede
            document.getElementById("motivo_m").value = motivo
            document.getElementById("fecha_r_m").value = fecha_retiro
        
            $('#updpersonalmovimiento').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});




//  CONSULTA DE PERSONAL POR ENTER

document.getElementById("inputCedula").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("formConsulta").submit();
    }
});

function MostrarEdades1() {
    let hijos = document.getElementById('hijos').value;
    if (hijos == "SI") {
        div = document.getElementById('edades1');
        div.style.display = 'block';
    } else {
        div = document.getElementById('edades1');
        div.style.display = 'none';
    }
}
function MostrarEdades2() {
    let hijos = document.getElementById('hijos2').value;
    if (hijos == "SI") {
        div = document.getElementById('edades2');
        div.style.display = 'block';
    } else {
        div = document.getElementById('edades2');
        div.style.display = 'none';
    }
}
function MostrarEdades3() {
    let hijos = document.getElementById('hijos3').value;
    if (hijos == "SI") {
        div = document.getElementById('edades3');
        div.style.display = 'block';
    } else {
        div = document.getElementById('edades3');
        div.style.display = 'none';
    }
}
function MostrarEdades4() {
    let hijos = document.getElementById('hijos4').value;
    if (hijos == "SI") {
        div = document.getElementById('edades4');
        div.style.display = 'block';
    } else {
        div = document.getElementById('edades4');
        div.style.display = 'none';
    }
}
function MostrarConyugue() {
    let hijos = document.getElementById('conyugue').value;
    if (hijos == "SI") {
        div = document.getElementById('conyugue1');
        div.style.display = 'block';
    } else {
        div = document.getElementById('conyugue1');
        div.style.display = 'none';
    }
}

function MostrarConyugueEditar() {
    let hijos = document.getElementById('conyugue_e').value;
    if (hijos == "true") {
        div = document.getElementById('conyugue1_e');
        div.style.display = 'block';
    } else {
        div = document.getElementById('conyugue1_e');
        div.style.display = 'none';
    }
}

function obtenerEdad(){

    let fechaNacimiento = document.getElementById('fecha_nac').value;
    fechaNacimiento =  new Date(fechaNacimiento);
    let edad = calcularEdad(fechaNacimiento);
    document.getElementById('edadadd').value= edad;
}

function calcularEdad(fechaNacimiento) {
    
    var hoy = new Date();
    var edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
    var mes = hoy.getMonth() - fechaNacimiento.getMonth();
    if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
      edad--;
    }
    return edad;
    
}

function MostrarBeneficiarios() {
    let fasmij = document.getElementById('fasmij').value;
    if (fasmij == 1) {
        div = document.getElementById('parentezco1');
        div.style.display = 'block';
        div = document.getElementById('beneficiario1');
        div.style.display = 'block';
        div = document.getElementById('cedula1');
        div.style.display = 'block';
        div = document.getElementById('direccion1');
        div.style.display = 'block';
        div = document.getElementById('parentezco2');
        div.style.display = 'block';
        div = document.getElementById('beneficiario2');
        div.style.display = 'block';
        div = document.getElementById('cedula2');
        div.style.display = 'block';
        div = document.getElementById('direccion2');
        div.style.display = 'block';
        div = document.getElementById('parentezco3');
        div.style.display = 'block';
        div = document.getElementById('beneficiario3');
        div.style.display = 'block';
        div = document.getElementById('cedula3');
        div.style.display = 'block';
        div = document.getElementById('direccion3');
        div.style.display = 'block';
    } else {
        div = document.getElementById('parentezco1');
        div.style.display = 'none';
        div = document.getElementById('beneficiario1');
        div.style.display = 'none';
        div = document.getElementById('cedula1');
        div.style.display = 'none';
        div = document.getElementById('direccion1');
        div.style.display = 'none';
        div = document.getElementById('parentezco2');
        div.style.display = 'none';
        div = document.getElementById('beneficiario2');
        div.style.display = 'none';
        div = document.getElementById('cedula2');
        div.style.display = 'none';
        div = document.getElementById('direccion2');
        div.style.display = 'none';
        div = document.getElementById('parentezco3');
        div.style.display = 'none';
        div = document.getElementById('beneficiario3');
        div.style.display = 'none';
        div = document.getElementById('cedula3');
        div.style.display = 'none';
        div = document.getElementById('direccion3');
        div.style.display = 'none';
       
    }
}