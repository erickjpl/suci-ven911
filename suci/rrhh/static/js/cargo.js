//  JAVASCRIPT PARA ADD CARGO

$(document).ready(function() {
    $('#myBtnAddCargo').click(function() {
        $('#addcargo').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE CARGO

$('.btn-editar').click(function() {

    let id_cargo = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-cargo-edicion/' + id_cargo,
        method: 'GET',
        success: function(response) {
            
            let id_cargo = response.id;
            let estatus = response.estatus;
            let cargo = response.cargo;
            
            document.getElementById("id_e").value = id_cargo;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("cargo_e").value = cargo;
            
        
            $('#updcargo').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
});