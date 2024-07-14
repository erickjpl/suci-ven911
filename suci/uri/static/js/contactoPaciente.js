//  JAVASCRIPT PARA ADD TALLA DE CAMISA

$(document).ready(function() {
    $('#addContacto').click(function() {
        $('#addContactoP').modal('show');
    });
});

//  JAVASCRIPT PARA UPDATE TALLA DE CAMISA

$('.btn-editar').click(function() {

    let id_contacto = $(this).data('id');
    
    $.ajax({
        url: '/uri/obtener-datos-contacto-edicion/' + id_contacto,
        method: 'GET',
        success: function(response) {
            
            let id_contacto = response.id;
            let contacto = response.contacto;
            
            document.getElementById("id_e").value = id_contacto;
            document.getElementById("contacto_e").value = contacto;
            
            $('#updContacto').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});

