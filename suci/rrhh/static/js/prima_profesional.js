//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addPrima').click(function() {
        $('#addPrimaProfesional').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_prima = $(this).data('id');
    $.ajax({
        url: '/rrhh/obtener_datos_prima_edicion/' + id_prima,
        method: 'GET',
        success: function(response) {
            
            let id_prima = response.id;
            let estatus = response.estatus;
            let titulo = response.titulo;
            let porcentaje = response.porcentaje;
            
            document.getElementById("id_e").value = id_prima;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("titulo_e").value = titulo;
            document.getElementById("porcentaje_e").value = porcentaje;
            
        
            $('#updPrima').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

