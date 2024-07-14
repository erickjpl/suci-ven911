//  JAVASCRIPT PARA ADD TALLA DE CAMISA

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_bono = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-bono-edicion/' + id_bono,
        method: 'GET',
        success: function(response) {
            
            let id_bono = response.id;
            let estatus = response.estatus;
            let descripcion = response.descripcion;
            let monto = response.monto;
            
            document.getElementById("id_e").value = id_bono;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("descripcion_e").value = descripcion;
            document.getElementById("monto_e").value = monto;
            
        
            $('#updBonoGuerra').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

