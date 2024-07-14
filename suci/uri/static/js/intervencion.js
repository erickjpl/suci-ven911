//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addIntervencion').click(function() {
        $('#addIntervenciones').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_intervencion = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-intervencion-edicion/' + id_intervencion,
        method: 'GET',
        success: function(response) {
            
            let id_intervencion = response.id;
            let intervencion = response.intervencion;
            
            document.getElementById("id_e").value = id_intervencion;
            document.getElementById("intervencion_e").value = intervencion;
            
            $('#updIntervencion').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

