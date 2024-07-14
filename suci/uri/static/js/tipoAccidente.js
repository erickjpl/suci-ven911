//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addAccidente').click(function() {
        $('#addTipoAccidente').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_tipoA = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-tipo-accidente-edicion/' + id_tipoA,
        method: 'GET',
        success: function(response) {
            
            let id_tipoA = response.id;
            let tipo_accidente = response.servicio;
            
            document.getElementById("id_e").value = id_tipoA;
            document.getElementById("tipo_accidente_e").value = tipo_accidente;
            
            $('#updTipoAccidente').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

