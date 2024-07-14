
//  JAVASCRIPT PARA ADD PERSONAL

$(document).ready(function() {
    $('#myBtnAdd').click(function() {
        $('#addbienes').modal('show');
    });
});


//  JAVASCRIPT PARA UPDATE PERSONAL

$('.btn-editar').click(function() {

    let id_bien = $(this).data('id');
    
    $.ajax({
        url: '/rrhh/obtener-datos-bienes-edicion/' + id_bien,
        method: 'GET',
        success: function(response) {
            
            let id_bien = response.id;
            let estatus = response.estatus;
            let nombre = response.nombre;
            let cantidad = response.cantidad;
            let departamento = response.departamento;
            let sede = response.sede;
            
            document.getElementById("id_e").value = id_bien;
            document.getElementById("estatus_e").value = estatus;
            document.getElementById("nombre_e").value = nombre;
            document.getElementById("cantidad_e").value = cantidad;
            document.getElementById("departamento_e").value = departamento;
            document.getElementById("sede_e").value = sede;
            
        
            $('#updbienes').modal('show');
        },
        error: function(error) {
            alert("Error al cargar los datos");
        }
    });
    
});


//  CONSULTA DE PERSONAL POR ENTER

document.getElementById("inputNombre").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("formConsulta").submit();
    }
});

const filtro = () => {
    
    let accion = "todos";
    let departamentofilter = document.getElementById("departamento_filtro").value
    
    var url = "/rrhh/bienes/"+ accion +  "/" + departamentofilter ;
    window.location.href = url;
      
}