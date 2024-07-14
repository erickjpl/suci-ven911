//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addReportes').click(function() {
        $('#addReporte').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_reporte = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-reportes-edicion/' + id_reporte,
        method: 'GET',
        success: function(response) {
            
            let id_reporte = response.id;
            let reporte = response.reporte;
            
            document.getElementById("id_e").value = id_reporte;
            document.getElementById("reporte_e").value = reporte;
            
            $('#updReporte').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

