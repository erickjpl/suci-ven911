//  JAVASCRIPT PARA ADD GRADO DE INSTRUCCION

$(document).ready(function() {
    $('#myBtnAdd').click(function() {
        $('#addDepartamento').modal('show');
    });
});


//  JAVASCRIPT PARA UPDATE TALLA DE DEPARTAMENTO

$('.btn-editar').click(function() {

    let id_departamento = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-departamento-edicion/' + id_departamento,
        method: 'GET',
        success: function(response) {
            
            let id_departamento = response.id;
            let estatus = response.estatus;
            let departamento = response.departamento;
            
            document.getElementById("id_e").value = id_departamento;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("departamento_e").value = departamento;
            
        
            $('#updDepartamento').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});
