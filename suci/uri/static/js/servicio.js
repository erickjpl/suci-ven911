//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addServicios').click(function() {
        $('#addServicio').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_servicio = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-servicios-edicion/' + id_servicio,
        method: 'GET',
        success: function(response) {
            
            let id_servicio = response.id;
            let servicio = response.servicio;
            
            document.getElementById("id_e").value = id_servicio;
            document.getElementById("servicio_e").value = servicio;
            
            $('#updServicio').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

