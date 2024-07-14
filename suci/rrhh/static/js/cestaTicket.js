//  JAVASCRIPT PARA ADD TALLA DE CAMISA

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_cesta = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-cestaticket-edicion/' + id_cesta,
        method: 'GET',
        success: function(response) {
            
            let id_cesta = response.id;
            let estatus = response.estatus;
            let descripcion = response.descripcion;
            let monto = response.monto;
            
            document.getElementById("id_e").value = id_cesta;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("descripcion_e").value = descripcion;
            document.getElementById("monto_e").value = monto;
            
        
            $('#updCestaTicket').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

