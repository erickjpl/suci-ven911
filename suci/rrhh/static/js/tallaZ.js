//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#myBtnAddZapato').click(function() {
        $('#addTallaZapato').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_talla = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-tallaZ-edicion/' + id_talla,
        method: 'GET',
        success: function(response) {
            
            let id_talla = response.id;
            let estatus = response.estatus;
            let talla = response.talla;
            
            document.getElementById("id_e").value = id_talla;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("talla_zapato_e").value = talla;
            
        
            $('#updTallaZapato').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

