//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addTraslados').click(function() {
        $('#addTraslado').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_traslado = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-traslados-edicion/' + id_traslado,
        method: 'GET',
        success: function(response) {
            
            let id_traslado = response.id;
            let traslado = response.traslado;
            
            document.getElementById("id_e").value = id_traslado;
            document.getElementById("traslado_e").value = traslado;
            
            $('#updTraslado').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

