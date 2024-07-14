//  JAVASCRIPT PARA ADD DENUNCIAS

$(document).ready(function() {
    $('#myBtnAdd').click(function() {
        $('#adddenuncia').modal('show');
    });
});


//  JAVASCRIPT PARA UPDATE DENUNCIAS

$('.btn-editar').click(function() {

    let id_denuncia = $(this).data('id');
    
    $.ajax({
        url: '/asesoria/obtener-datos-denuncia-edicion/' + id_denuncia,
        method: 'GET',
        success: function(response) {
            
            let id_denuncia = response.id;
            let estatus = response.estatus;
            let ente = response.ente;
            let nombre_d = response.nombres_d;
            let apellido_d = response.apellidos_d;
            let cedula_d = response.cedula_d;
            let telefono = response.telefono;
            let email = response.email;
            let direccion_d = response.direccion_d;
            let nombre_denunciado = response.nombres_denunciado;
            let apellido_denunciados = response.apellidos_denunciado;
            let cedula_denunciado = response.cedula_denunciado;
            let motivo = response.motivo;
            let zona = response.zona;
            let fecha_denuncia = response.fecha_denuncia;
            let fecha_incidente = response.fecha_incidente;
            
            
            document.getElementById("id_e").value = id_denuncia;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("ente_e").value = ente;
            document.getElementById("nombres_d_e").value = nombre_d;
            document.getElementById("apellidos_d_e").value = apellido_d;
            document.getElementById("cedula_d_e").value = cedula_d;
            document.getElementById("telefono_d_e").value = telefono;
            document.getElementById("correo_e").value = email;
            document.getElementById("direccion_e").value = direccion_d;
            document.getElementById("nombres_denunciado_e").value = nombre_denunciado;
            document.getElementById("apellidos_denunciado_e").value = apellido_denunciados;
            document.getElementById("cedula_denunciado_e").value = cedula_denunciado;
            document.getElementById("motivo_e").value = motivo;
            document.getElementById("zona_e").value = zona;
            document.getElementById("fecha_incidente_e").value = fecha_incidente;
            document.getElementById("fecha_denuncia_e").value = fecha_denuncia;
            
        
            $('#updDenuncia').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

