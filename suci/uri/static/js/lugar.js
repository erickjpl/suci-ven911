//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addLugares').click(function() {
        $('#addLugar').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_lugar = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-lugares-edicion/' + id_lugar,
        method: 'GET',
        success: function(response) {
            
            let id_lugar = response.id;
            let lugar = response.lugar;
            
            document.getElementById("id_e").value = id_lugar;
            document.getElementById("lugar_e").value = lugar;
            
            $('#updLugar').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

