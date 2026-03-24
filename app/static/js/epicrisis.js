/* Cargar datos de paciente en form */
const $codigo = document.getElementById("codigo");
const $paciente = document.getElementById("paciente");
const $tablaModalPacientes = document.getElementById("tablaModalPacientes");

$tablaModalPacientes.addEventListener("click", (e) => {
    e.stopPropagation();
    let data = e.target.parentElement.children;
    fillDataPaciente(data);
    closeAllModals();
})

const fillDataPaciente = (data) => {
    $codigo.value = data[0].innerText;
    $paciente.value = data[1].innerText;
}

/* Cargar datos de evolucion en form */
const $evolucion_clinica = document.getElementById("evolucion_clinica");
const $tablaModalEvoluciones = document.getElementById("tablaModalEvoluciones");

$tablaModalEvoluciones.addEventListener("click", (e) => {
  e.stopPropagation();
  let data = e.target.parentElement.children;
  fillDataEvolucion(data);
  closeAllModals();
})

const fillDataEvolucion = (data) => {
  $evolucion_clinica.value = data[1].innerText;
}

/* Cargar datos de diagnosticos en form */
const $cod_diag = document.getElementById("cod_diag");
const $nom_diag = document.getElementById("nom_diag");
const $tablaModalDiagnosticos = document.getElementById("tablaModalDiagnosticos");

$tablaModalDiagnosticos.addEventListener("click", (e) => {
  e.stopPropagation();
  let data = e.target.parentElement.children;
  fillDataDiagnostico(data)
  closeAllModals();
})

const fillDataDiagnostico = (data) => {
  $cod_diag.value = data[0].innerText;
  $nom_diag.value = data[1].innerText;
};


/* Cerrar Modal */
function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

