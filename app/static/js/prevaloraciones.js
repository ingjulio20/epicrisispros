const $fechaAt = document.getElementById("fechaAt");
const $horaAt = document.getElementById("horaAt");

window.onload = () => {
    let fecha = new Date();
    /* Hora Actual */
    let hora = fecha.getHours(), minutos = fecha.getMinutes()
    /* Fecha Actual */
    let anio = fecha.getFullYear();
    let mes = fecha.getMonth() + 1;
    let dia = fecha.getDate();
    if(dia < 10){
        dia = "0" + dia;
    }
    if(mes < 10){
        mes = "0" + mes;
    }
    /* Cargar en Form */
    $fechaAt.value = anio + "-" + mes + "-" + dia
    $horaAt.value = hora + ":" + minutos
}

/* Cargar datos de paciente en Form */
const $documentoPac = document.getElementById("documentoPac");
const $nombrePac = document.getElementById("nombrePac");
const $tablaModalPacientes = document.getElementById("tablaModalPacientes");

$tablaModalPacientes.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataPaciente(data);
    closeAllModals();
})

const fillDataPaciente = (data) => {
    $documentoPac.value = data[0].innerText;
    $nombrePac.value = data[1].innerText;
}

/* Cargar datos de diagnosticos en Form */
const $codDiag1 = document.getElementById("codDiag1");
const $nomDiag1 = document.getElementById("nomDiag1");
const $codDiag2 = document.getElementById("codDiag2");
const $nomDiag2 = document.getElementById("nomDiag2");
const $codDiag3 = document.getElementById("codDiag3");
const $nomDiag3 = document.getElementById("nomDiag3");
const $tablaModalDiagnosticos = document.getElementById("tablaModalDiagnosticos");

$tablaModalDiagnosticos.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    if($codDiag1.value === '' && $nomDiag1.value === ''){
        $codDiag1.value = data[0].innerText;
        $nomDiag1.value = data[1].innerText;
    }else if($codDiag2.value === '' && $nomDiag2.value === ''){
        $codDiag2.value = data[0].innerText;
        $nomDiag2.value = data[1].innerText;
    }else if($codDiag3.value === '' && $nomDiag3.value === ''){
        $codDiag3.value = data[0].innerText;
        $nomDiag3.value = data[1].innerText;
    }
    closeAllModals();
})

/* Limpiar los campos de diagnosticos (Corregir) */
const $btnCorregir = document.getElementById("btnCorregir");
$btnCorregir.addEventListener("click", (e) => {
    e.preventDefault();
    $codDiag1.value = "";
    $nomDiag1.value = "";
    $codDiag2.value = "";
    $nomDiag2.value = "";
    $codDiag3.value = "";
    $nomDiag3.value = "";
})

/* Cerrar Modal */
function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }
