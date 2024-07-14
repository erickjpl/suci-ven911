
$(document).ready(function() {
    $('#addUri').click(function() {
        $('#addRegistro').modal('show');
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

let currentTab = 0;
showTab(currentTab);

function showTab(n) {
  let tabButtons = document.getElementsByClassName("tab-button-prehospitalario");
  let tabPanes = document.getElementsByClassName("tab-pane-prehospitalario");
  let prevNextButtons = document.getElementsByClassName("tab-buttons-prehospitalario")[1];
  let saveButton = document.getElementById("saveBtn");
  
  tabPanes[n].classList.add("active");
  tabButtons[n].classList.add("active");
  
  for (let i = 0; i < tabPanes.length; i++) {
    if (i !== n) {
      tabPanes[i].classList.remove("active");
      tabButtons[i].classList.remove("active");
    }
  }
  
  if (n == (tabPanes.length - 1)) {
    saveButton.style.display = "inline";
    document.getElementById("nextBtn").style.display = "none";
  } else {
    saveButton.style.display = "none";
    document.getElementById("nextBtn").style.display = "inline";
  }
}

function nextPrev(n) {
  let tabPanes = document.getElementsByClassName("tab-pane-prehospitalario");
  currentTab = currentTab + n;
  if (currentTab >= tabPanes.length) {
    if (!validateForm()) return false;
    submitForm();
    return false;
  }
  showTab(currentTab);
}

function validateForm() {
  let tabPanes = document.getElementsByClassName("tab-pane-prehospitalario");
  let valid = true;
  let inputs = tabPanes[currentTab].getElementsByTagName("input");
  for (let i = 0; i < inputs.length; i++) {
    if (inputs[i].value == "") {
      inputs[i].className += " invalid";
      valid = false;
    }
  }
  return valid;
}

function submitForm() {
  document.getElementById("registration-form").submit();
}


