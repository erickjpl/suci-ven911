//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addEvaluacion').click(function() {
        $('#addEvaluaciones').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_evaluacion = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-evaluacion-edicion/' + id_evaluacion,
        method: 'GET',
        success: function(response) {
            
            let id_evaluacion = response.id;
            let evaluacion = response.evaluacion;
            
            document.getElementById("id_e").value = id_evaluacion;
            document.getElementById("evaluacion_e").value = evaluacion;
            
            $('#updEvaluacion').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

