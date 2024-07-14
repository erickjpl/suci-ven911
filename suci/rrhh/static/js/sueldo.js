//  JAVASCRIPT PARA ADD CARGO

$(document).ready(function() {
    $('#myBtnAddCargo').click(function() {
        $('#addcargo').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE SUELDOS

$('.btn-editar').click(function() {

    let id_sueldo = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-sueldos-edicion/' + id_sueldo,
        method: 'GET',
        success: function(response) {
            
            let id_sueldo = response.id;
            let estatus = response.estatus;
            let sueldo_base = response.sueldo_base;
            let prima_profesionalismo = response.prima_profesionalismo;
            let p_discapacidad = response.p_discapacidad;
            let p_hijos_menor_12 = response.p_hijos_menor_12;
            let p_hijas_menor_12 = response.p_hijas_menor_12;
            let p_hijos_12_18 = response.p_hijos_12_18;
            let p_hijos_discapacidad = response.p_hijos_discapacidad;
            let n_fasmij = response.sueldo_base;
            let cesta_t = response.cesta_t;
            let monto_t = response.monto_t;
            let b_guerra = response.b_guerra;
            let monto_b = response.monto_b;
            let personal = response.personal;
            
            document.getElementById("id_e").value = id_sueldo;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("sueldo_base_e").value = sueldo_base;
            document.getElementById("prima_profesionalismo_e").value = prima_profesionalismo;
            document.getElementById("p_discapacidad_e").value = p_discapacidad;
            document.getElementById("p_hijos_discapacidad_e").value = p_hijos_discapacidad;
            document.getElementById("n_fasmij_e").value = n_fasmij;
            document.getElementById("monto_t_e").value = monto_t;
            document.getElementById("monto_b_e").value = monto_b;
            document.getElementById("personal_e").value = personal;
            
        
            $('#updSede').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
});