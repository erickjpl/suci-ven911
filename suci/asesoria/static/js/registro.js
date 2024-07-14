//  JAVASCRIPT PARA ADD DENUNCIAS

$(document).ready(function() {
    $('#myBtnAdd').click(function() {
        $('#addregistro').modal('show');
    });
});


//  JAVASCRIPT PARA UPDATE DENUNCIAS

$('.btn-editar').click(function() {

    let id_registro = $(this).data('id');
    
    $.ajax({
        url: '/asesoria/obtener-datos-registro-edicion/' + id_registro,
        method: 'GET',
        success: function(response) {
            
            let id_registro = response.id;
            let estatus = response.estatus;
            let direccion = response.direccion;
            let camara = response.camara;
            let motivo_solicitud = response.motivo_solicitud;
            let ente_solicita = response.ente_solicita;
            let fecha_solicitud = response.fecha_solicitud;
            let fecha_culminacion = response.fecha_culminacion;
            
            
            
            document.getElementById("id_e").value = id_registro;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("direccion_e").value = direccion;
            document.getElementById("camara_e").value = camara;
            document.getElementById("motivo_solicitud_e").value =motivo_solicitud;
            document.getElementById("ente_solicita_e").value = ente_solicita;
            document.getElementById("fecha_solicitud_e").value = fecha_solicitud;
            document.getElementById("fecha_culminacion_e").value = fecha_culminacion;
           
        
            $('#updregistro').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

