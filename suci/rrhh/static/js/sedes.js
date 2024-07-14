
//  JAVASCRIPT PARA ADD PERSONAL

$(document).ready(function() {
    $('#myBtnAddSedes').click(function() {
        $('#addSede').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE SEDE

$('.btn-editar').click(function() {

    let id_sede = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-sede-edicion/' + id_sede,
        method: 'GET',
        success: function(response) {
            
            let id_sede = response.id;
            let estatus = response.estatus;
            let sede = response.sede;
            
            document.getElementById("id_e").value = id_sede;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("sede_e").value = sede;
            
        
            $('#updSede').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});


