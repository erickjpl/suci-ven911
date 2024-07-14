let createUrl
let api
let method

function setup (conf) {
  createUrl = conf.hasOwnProperty('url') ? conf.url : ''
}

const setTBody = ({ listUrl, columns, updateUrl, deleteUrl }) => {
  $("#data-table").DataTable({
    resposive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    processing: true,
    serverSide: true,
    pageLength: 10,
    ajax: {
      url: listUrl,
      type: "GET",
      dataSrc: "entities",
      dataType: "json",
    },
    columns: columns,
    columnDefs: [
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          const rowStr = JSON.stringify(row).replace(/"/g, '&quot;');

          let buttons = `
            <ion-icon onclick="updateModal('${updateUrl}', ${rowStr})" name="create-outline" color="primary" style="font-size: 22px; cursor: pointer;"></ion-icon>
            <ion-icon onclick="destroyModal('${deleteUrl}', ${rowStr})" name="trash-outline" color="danger" style="font-size: 22px; cursor: pointer;"></ion-icon>
          `;
          return buttons;
        },
      },
    ],
    language: language,
  });
};

$('#add-btn').click(function () {
  sendView(createUrl)
});

function updateModal (url, data) {
  const updateUrl = url.replace('0', data.id)
  $("#form :input").each(function () {
    $(this).val(data[this.name]);
  });
  sendView(updateUrl)
}

function destroyModal (url, data) {
  const deleteUrl = url.replace('0', data.id)
  sendView(deleteUrl)
  $("#entity-id").text(data.id)
}

$('#delete-record').click(function () {
  $.ajax({
    url: api,
    type: method,
    dataType: 'json'
  })
    .done(function (data) {
      if (data.hasOwnProperty('errors')) {
        toastError('Alerta..!', 'Ha ocurrido un error..!')
        return false
      }

      success(data.message)
    })
    .fail((jqXHR, textStatus, errorThrown) => console.error({ jqXHR, textStatus, errorThrown }))
});

function sendView (url) {
  $.ajax({
    url: url,
    type: 'GET',
    dataType: 'json'
  })
    .done(staticDataModal)
    .fail((jqXHR, textStatus, errorThrown) => console.error({ jqXHR, textStatus, errorThrown }))
}

function staticDataModal ({ urlApi, methodForm, modalTitle }) {
  if (methodForm == 'DELETE')
    $("#modal-delete").modal('show')
  else
    $("#modal").modal('show')

  $(".modal-title").text(modalTitle)
  api = urlApi
  method = methodForm
}

$('form').on('submit', function (event) {
  event.preventDefault()
  console.info("HOLA")

  const data = $(this).serializeArray()
  $.ajax({
    url: api,
    type: method,
    data: data,
    dataType: 'json'
  })
    .done(function (data) {
      if (data.hasOwnProperty('errors')) {
        toastError('Alerta..!', 'Ha ocurrido un error..!')
        form_errors(data.errors)
        return false
      }

      success(data.message)
    })
    .fail((jqXHR, textStatus, errorThrown) => console.error({ jqXHR, textStatus, errorThrown }))
    .always(() => {
      Array.from(document.querySelectorAll('.form-control.is-invalid')).forEach((el) => el.classList.remove('is-invalid'))
    })
})

function success (message) {
  $("#modal-delete").modal('hide')
  $("#modal").modal('hide')
  $('form').trigger('reset')
  toastSuccess('Excelente..!', message)
  document.getElementById('form').classList.remove('was-validated')
}

let language = {
  aria: {
    sortAscending: "Activar para ordenar la columna de manera ascendente",
    sortDescending: "Activar para ordenar la columna de manera descendente",
  },
  autoFill: {
    cancel: "Cancelar",
    fill: "Rellene todas las celdas con <i>%d</i>",
    fillHorizontal: "Rellenar celdas horizontalmente",
    fillVertical: "Rellenar celdas verticalmente",
  },
  buttons: {
    collection: "Colección",
    colvis: "Visibilidad",
    colvisRestore: "Restaurar visibilidad",
    copy: "Copiar",
    copyKeys:
      "Presione ctrl o u2318 + C para copiar los datos de la tabla al portapapeles del sistema. <br /> <br /> Para cancelar, haga clic en este mensaje o presione escape.",
    copySuccess: {
      1: "Copiada 1 fila al portapapeles",
      _: "Copiadas %d fila al portapapeles",
    },
    copyTitle: "Copiar al portapapeles",
    csv: "CSV",
    excel: "Excel",
    pageLength: {
      "-1": "Mostrar todas las filas",
      _: "Mostrar %d filas",
    },
    pdf: "PDF",
    print: "Imprimir",
    createState: "Crear Estado",
    removeAllStates: "Borrar Todos los Estados",
    removeState: "Borrar Estado",
    renameState: "Renombrar Estado",
    savedStates: "Guardar Estado",
    stateRestore: "Restaurar Estado",
    updateState: "Actualizar Estado",
  },
  infoThousands: ",",
  loadingRecords: "Cargando...",
  paginate: {
    first: "Primero",
    last: "Último",
    next: "Siguiente",
    previous: "Anterior",
  },
  processing: "Procesando...",
  search: "Buscar:",
  searchBuilder: {
    add: "Añadir condición",
    button: {
      0: "Constructor de búsqueda",
      _: "Constructor de búsqueda (%d)",
    },
    clearAll: "Borrar todo",
    condition: "Condición",
    deleteTitle: "Eliminar regla de filtrado",
    leftTitle: "Criterios anulados",
    logicAnd: "Y",
    logicOr: "O",
    rightTitle: "Criterios de sangría",
    title: {
      0: "Constructor de búsqueda",
      _: "Constructor de búsqueda (%d)",
    },
    value: "Valor",
    conditions: {
      date: {
        after: "Después",
        before: "Antes",
        between: "Entre",
        empty: "Vacío",
        equals: "Igual a",
        not: "Diferente de",
        notBetween: "No entre",
        notEmpty: "No vacío",
      },
      number: {
        between: "Entre",
        empty: "Vacío",
        equals: "Igual a",
        gt: "Mayor a",
        gte: "Mayor o igual a",
        lt: "Menor que",
        lte: "Menor o igual a",
        not: "Diferente de",
        notBetween: "No entre",
        notEmpty: "No vacío",
      },
      string: {
        contains: "Contiene",
        empty: "Vacío",
        endsWith: "Termina con",
        equals: "Igual a",
        not: "Diferente de",
        startsWith: "Inicia con",
        notEmpty: "No vacío",
        notContains: "No Contiene",
        notEnds: "No Termina",
        notStarts: "No Comienza",
      },
      array: {
        equals: "Igual a",
        empty: "Vacío",
        contains: "Contiene",
        not: "Diferente",
        notEmpty: "No vacío",
        without: "Sin",
      },
    },
    data: "Datos",
  },
  searchPanes: {
    clearMessage: "Borrar todo",
    collapse: {
      0: "Paneles de búsqueda",
      _: "Paneles de búsqueda (%d)",
    },
    count: "{total}",
    emptyPanes: "Sin paneles de búsqueda",
    loadMessage: "Cargando paneles de búsqueda",
    title: "Filtros Activos - %d",
    countFiltered: "{shown} ({total})",
    collapseMessage: "Colapsar",
    showMessage: "Mostrar Todo",
  },
  select: {
    cells: {
      1: "1 celda seleccionada",
      _: "%d celdas seleccionadas",
    },
    columns: {
      1: "1 columna seleccionada",
      _: "%d columnas seleccionadas",
    },
  },
  thousands: ",",
  datetime: {
    previous: "Anterior",
    hours: "Horas",
    minutes: "Minutos",
    seconds: "Segundos",
    unknown: "-",
    amPm: ["am", "pm"],
    next: "Siguiente",
    months: {
      0: "Enero",
      1: "Febrero",
      2: "Marzo",
      3: "Abril",
      4: "Mayo",
      5: "Junio",
      6: "Julio",
      7: "Agosto",
      8: "Septiembre",
      9: "Octubre",
      10: "Noviembre",
      11: "Diciembre",
    },
    weekdays: [
      "Domingo",
      "Lunes",
      "Martes",
      "Miércoles",
      "Jueves",
      "Viernes",
      "Sábado",
    ],
  },
  editor: {
    close: "Cerrar",
    create: {
      button: "Nuevo",
      title: "Crear Nuevo Registro",
      submit: "Crear",
    },
    edit: {
      button: "Editar",
      title: "Editar Registro",
      submit: "Actualizar",
    },
    remove: {
      button: "Eliminar",
      title: "Eliminar Registro",
      submit: "Eliminar",
      confirm: {
        1: "¿Está seguro que desea eliminar 1 fila?",
        _: "¿Está seguro que desea eliminar %d filas?",
      },
    },
    multi: {
      title: "Múltiples Valores",
      restore: "Deshacer Cambios",
      noMulti:
        "Este registro puede ser editado individualmente, pero no como parte de un grupo.",
      info: "Los elementos seleccionados contienen diferentes valores para este registro. Para editar y establecer todos los elementos de este registro con el mismo valor, haga click o toque aquí, de lo contrario conservarán sus valores individuales.",
    },
    error: {
      system: "Ha ocurrido un error en el sistema.",
    },
  },
  decimal: ".",
  emptyTable: "No hay datos disponibles en la tabla",
  zeroRecords: "No se encontraron coincidencias",
  info: "Mostrando _START_ a _END_ de _TOTAL_ entradas",
  infoEmpty: "Mostrando 0 a 0 de 0 entradas",
  infoFiltered: "(Filtrado de _MAX_ total de entradas)",
  lengthMenu: "Mostrar _MENU_ entradas",
  stateRestore: {
    removeTitle: "Eliminar",
    creationModal: {
      search: "Busccar",
    },
  },
};

function prepare (title, message, date) {
  // const toastHtml = document.getElementById('toast')
  document.getElementById('toast-title').textContent = title
  // document.getElementById('toast-date').textContent = date
  document.getElementById('toast-message').textContent = message
  // const toast = new bootstrap.Toast(toastHtml)
  $("#toast").toast("show")
  // toast.show()
}

function toast (title, message, date = 'Hace un momento') {
  prepare(title, message, date)
}

function toastSecondary (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary', `bg-info`, `bg-success`, 'bg-warning', 'bg-danger').addClass(`bg-secondary`)
  prepare(title, message, date)
}

function toastInfo (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary', `bg-secondary`, `bg-success`, 'bg-warning', 'bg-danger').addClass(`bg-info`)
  prepare(title, message, date)
}

function toastSuccess (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary', `bg-secondary`, `bg-info`, 'bg-warning', 'bg-danger').addClass(`bg-success`)
  prepare(title, message, date)
}

function toastWarning (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary', `bg-secondary`, `bg-info`, 'bg-success', 'bg-danger').addClass(`bg-warning`)
  prepare(title, message, date)
}

function toastError (title, message, date = 'Hace un momento') {
  $('#toast').removeClass('bg-primary', `bg-secondary`, `bg-info`, 'bg-success', 'bg-warning').addClass(`bg-danger`)
  prepare(title, message, date)
}

function form_errors (errors) {
  $.each(errors, function (key, value) {
    console.info({ key, value })
    const input = $(`#${key}_id`);
    input.addClass("is-invalid");
    input.next().text(value[0].message);
  });
}

// Validar el formulario por parte del cliente
(function () {
  "use strict";
  const form = document.getElementById("form");

  form.addEventListener(
    "submit",
    function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }

      form.classList.add("was-validated");
    },
    false
  );
})();