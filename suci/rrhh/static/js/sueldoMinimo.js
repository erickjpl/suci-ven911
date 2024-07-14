//  JAVASCRIPT PARA ADD TALLA DE CAMISA

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_sueldo = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener_datos_sueldominimo_edicion/' + id_sueldo,
        method: 'GET',
        success: function(response) {
            
            let id_sueldo = response.id;
            let estatus = response.estatus;
            let descripcion = response.descripcion;
            let monto = response.monto;
            
            document.getElementById("id_e").value = id_sueldo;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("descripcion_e").value = descripcion;
            document.getElementById("monto_e").value = monto;
            
        
            $('#updSueldoMinimo').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

