//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addtipoA').click(function() {
        $('#addTipoArma').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_tipoA = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-tipo-arma-edicion/' + id_tipoA,
        method: 'GET',
        success: function(response) {
            
            let id_tipoA= response.id;
            let tipo_arma = response.tipo_arma;
            
            document.getElementById("id_e").value = id_tipoA;
            document.getElementById("tipo_arma_e").value = tipo_arma;
            
            $('#updTipoArma').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

