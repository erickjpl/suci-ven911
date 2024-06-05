function mostrarErroresCreacion (errores) {
  $('#errores').html("");
  let error = "";
  for (let item in errores.responseJSON.error) {
    error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
  }
  $('#errores').append(error);
}

function mostrarErroresEdicion (errores) {
  $('#erroresEdicion').html("");
  let error = "";
  for (let item in errores.responseJSON.error) {
    error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
  }
  $('#erroresEdicion').append(error);
}

function notificacionError (mensaje) {
  Swal.fire({
    title: 'Error!',
    text: mensaje,
    icon: 'error'
  })
}

function notificacionSuccess (mensaje) {
  Swal.fire({
    title: 'Buen Trabajo!',
    text: mensaje,
    icon: 'success'
  })
}