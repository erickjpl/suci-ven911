function getCookie (name) {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  if (match)
    return match[2];
}

function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
  }
});

function form_errors (errors) {
  console.error(errors)
  $.each(errors, function (key, value) {
    const input = $(`#id_${key}`)
    input.addClass('is-invalid');
    input.next().text(value[0].message)    
  });
}
